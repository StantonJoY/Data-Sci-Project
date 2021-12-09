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
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_is_zero', asname=None),
                alias(name='float_repr', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='product.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='product.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cost_method', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='categ_id.property_cost_method', kind=None),
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
                    targets=[Name(id='valuation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='categ_id.property_valuation', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='impacted_templates', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Product', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.product', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='SVL', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.valuation.layer', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='categ_id', kind=None),
                                ops=[In()],
                                comparators=[Name(id='vals', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_product_category', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.category', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='categ_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='product_template', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='product_template', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='product_template', ctx=Load()),
                                                    attr='with_company',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='product_template', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='valuation_impacted', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='product_template', ctx=Load()),
                                                    attr='cost_method',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='new_product_category', ctx=Load()),
                                                        attr='property_cost_method',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='valuation_impacted', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='product_template', ctx=Load()),
                                                    attr='valuation',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='new_product_category', ctx=Load()),
                                                        attr='property_valuation',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='valuation_impacted', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='valuation_impacted', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='description', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Due to a change of product category (from %s to %s), the costing method                                has changed for product template %s: from %s to %s.', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='product_template', ctx=Load()),
                                                                attr='categ_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='new_product_category', ctx=Load()),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='product_template', ctx=Load()),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='product_template', ctx=Load()),
                                                            attr='cost_method',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='new_product_category', ctx=Load()),
                                                            attr='property_cost_method',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='out_svl_vals_list', ctx=Store()),
                                                        Name(id='products_orig_quantity_svl', ctx=Store()),
                                                        Name(id='products', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Product', ctx=Load()),
                                                    attr='_svl_empty_stock',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='description', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='product_template',
                                                        value=Name(id='product_template', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='out_stock_valuation_layers', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='SVL', ctx=Load()),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='out_svl_vals_list', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='product_template', ctx=Load()),
                                                    attr='valuation',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='real_time', kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='move_vals_list', ctx=Store()),
                                                    op=Add(),
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Product', ctx=Load()),
                                                            attr='_svl_empty_stock_am',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='out_stock_valuation_layers', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='impacted_templates', ctx=Load()),
                                                    slice=Name(id='product_template', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='products', ctx=Load()),
                                                    Name(id='description', ctx=Load()),
                                                    Name(id='products_orig_quantity_svl', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProductTemplate', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='product_template', ctx=Store()),
                                    Tuple(
                                        elts=[
                                            Name(id='products', ctx=Store()),
                                            Name(id='description', ctx=Store()),
                                            Name(id='products_orig_quantity_svl', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='impacted_templates', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='in_svl_vals_list', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='products', ctx=Load()),
                                            attr='_svl_replenish_stock',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='description', ctx=Load()),
                                            Name(id='products_orig_quantity_svl', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='in_stock_valuation_layers', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='SVL', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='in_svl_vals_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='product_template', ctx=Load()),
                                            attr='valuation',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='real_time', kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='move_vals_list', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Product', ctx=Load()),
                                                    attr='_svl_replenish_stock_am',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='in_stock_valuation_layers', ctx=Load())],
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='move_vals_list', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='stock.valuation.layer', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='check_access_rights',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='read', kind=None)],
                                            keywords=[
                                                keyword(
                                                    arg='raise_exception',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="The action leads to the creation of a journal entry, for which you don't have the access rights.", kind=None)],
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
                        If(
                            test=Name(id='move_vals_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='account_moves', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='move_vals_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='account_moves', ctx=Load()),
                                            attr='_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                        Expr(
                            value=Constant(value=' Add the stock accounts related to product to the result of super()\n        @return: dictionary which contains information regarding stock accounts and super (income+expense accounts)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='accounts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProductTemplate', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_product_accounts',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_asset_accounts',
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
                                    value=Name(id='accounts', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='stock_input', kind=None),
                                            Constant(value='stock_output', kind=None),
                                            Constant(value='stock_valuation', kind=None),
                                        ],
                                        values=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='stock_input', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='categ_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='property_stock_account_input_categ_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='stock_output', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='categ_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='property_stock_account_output_categ_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='categ_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='property_stock_valuation_account_id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='accounts', ctx=Load()),
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
                        Expr(
                            value=Constant(value=' Add the stock journal related to product to the result of super()\n        @return: dictionary which contains all needed information regarding stock accounts and journal and super (income+expense accounts)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='accounts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProductTemplate', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_product_accounts',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fiscal_pos',
                                        value=Name(id='fiscal_pos', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='accounts', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='stock_journal', kind=None)],
                                        values=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='categ_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='property_stock_journal',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='accounts', ctx=Load()),
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
                    targets=[Name(id='value_svl', ctx=Store())],
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
                                value=Constant(value='_compute_value_svl', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='quantity_svl', ctx=Store())],
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
                                value=Constant(value='_compute_value_svl', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stock_valuation_layer_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.valuation.layer', kind=None),
                            Constant(value='product_id', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='valuation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='categ_id.property_valuation', kind=None),
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
                    targets=[Name(id='cost_method', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='categ_id.property_cost_method', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='standard_price', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
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
                                            args=[Constant(value='disable_auto_svl', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
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
                                                            args=[arg(arg='p', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='p', ctx=Load()),
                                                                attr='cost_method',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotEq()],
                                                            comparators=[Constant(value='fifo', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_change_standard_price',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='standard_price', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                                            Name(id='ProductProduct', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_value_svl',
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
                            value=Constant(value='Compute `value_svl` and `quantity_svl`.', kind=None),
                        ),
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
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='company_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
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
                                args=[Constant(value='to_date', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='to_date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='to_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='to_date', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='create_date', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='to_date', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.valuation.layer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='value:sum', kind=None),
                                            Constant(value='quantity:sum', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='product_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='products', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='group', ctx=Store()),
                            iter=Name(id='groups', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='group', ctx=Load()),
                                                    slice=Constant(value='product_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='value_svl',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
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
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='group', ctx=Load()),
                                                slice=Constant(value='value', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='quantity_svl',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='group', ctx=Load()),
                                        slice=Constant(value='quantity', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='products', ctx=Store()),
                                    op=BitOr(),
                                    value=Name(id='product', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remaining', ctx=Store())],
                            value=BinOp(
                                left=Name(id='self', ctx=Load()),
                                op=Sub(),
                                right=Name(id='products', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='remaining', ctx=Load()),
                                    attr='value_svl',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='remaining', ctx=Load()),
                                    attr='quantity_svl',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
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
                            args=[Constant(value='stock_valuation_layer_ids', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends_context',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='to_date', kind=None),
                                Constant(value='company', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_revaluation',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='default_product_id',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='default_company_id',
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
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='view_id', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Product Revaluation', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='form', kind=None),
                                    Constant(value='stock.valuation.layer.revaluation', kind=None),
                                    Attribute(
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
                                            args=[Constant(value='stock_account.stock_valuation_layer_revaluation_form_view', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Name(id='ctx', ctx=Load()),
                                    Constant(value='new', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_in_svl_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='quantity', annotation=None, type_comment=None),
                            arg(arg='unit_cost', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Prepare the values for a stock valuation layer created by a receipt.\n\n        :param quantity: the quantity to value, expressed in `self.uom_id`\n        :param unit_cost: the unit cost to value `quantity`\n        :return: values to use in a call to create\n        :rtype: dict\n        ', kind=None),
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
                            targets=[Name(id='vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='product_id', kind=None),
                                    Constant(value='value', kind=None),
                                    Constant(value='unit_cost', kind=None),
                                    Constant(value='quantity', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='unit_cost', ctx=Load()),
                                        op=Mult(),
                                        right=Name(id='quantity', ctx=Load()),
                                    ),
                                    Name(id='unit_cost', ctx=Load()),
                                    Name(id='quantity', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cost_method',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='average', kind=None),
                                            Constant(value='fifo', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='remaining_qty', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='quantity', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='remaining_value', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='vals', ctx=Load()),
                                        slice=Constant(value='value', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_out_svl_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='quantity', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Prepare the values for a stock valuation layer created by a delivery.\n\n        :param quantity: the quantity to value, expressed in `self.uom_id`\n        :return: values to use in a call to create\n        :rtype: dict\n        ', kind=None),
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
                            targets=[Name(id='quantity', ctx=Store())],
                            value=BinOp(
                                left=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                op=Mult(),
                                right=Name(id='quantity', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='product_id', kind=None),
                                    Constant(value='value', kind=None),
                                    Constant(value='unit_cost', kind=None),
                                    Constant(value='quantity', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='quantity', ctx=Load()),
                                        op=Mult(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='standard_price',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='standard_price',
                                        ctx=Load(),
                                    ),
                                    Name(id='quantity', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cost_method',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='average', kind=None),
                                            Constant(value='fifo', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fifo_vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_run_fifo',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='abs', ctx=Load()),
                                                args=[Name(id='quantity', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='company', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='remaining_qty', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fifo_vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='remaining_qty', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='cost_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='average', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='currency', ctx=Store())],
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
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='rounding_error', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='round',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='standard_price',
                                                                ctx=Load(),
                                                            ),
                                                            op=Mult(),
                                                            right=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='quantity_svl',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='value_svl',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='rounding_error', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='abs', ctx=Load()),
                                                            args=[Name(id='rounding_error', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ops=[LtE()],
                                                        comparators=[
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Call(
                                                                        func=Name(id='abs', ctx=Load()),
                                                                        args=[Name(id='quantity', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    op=Mult(),
                                                                    right=Attribute(
                                                                        value=Name(id='currency', ctx=Load()),
                                                                        attr='rounding',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                op=Div(),
                                                                right=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Subscript(
                                                                value=Name(id='vals', ctx=Load()),
                                                                slice=Constant(value='value', kind=None),
                                                                ctx=Store(),
                                                            ),
                                                            op=Add(),
                                                            value=Name(id='rounding_error', ctx=Load()),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='vals', ctx=Load()),
                                                                    slice=Constant(value='rounding_adjustment', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BinOp(
                                                                left=Constant(value='\nRounding Adjustment: %s%s %s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        IfExp(
                                                                            test=Compare(
                                                                                left=Name(id='rounding_error', ctx=Load()),
                                                                                ops=[Gt()],
                                                                                comparators=[Constant(value=0, kind=None)],
                                                                            ),
                                                                            body=Constant(value='+', kind=None),
                                                                            orelse=Constant(value='', kind=None),
                                                                        ),
                                                                        Call(
                                                                            func=Name(id='float_repr', ctx=Load()),
                                                                            args=[Name(id='rounding_error', ctx=Load())],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='precision_digits',
                                                                                    value=Attribute(
                                                                                        value=Name(id='currency', ctx=Load()),
                                                                                        attr='decimal_places',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='currency', ctx=Load()),
                                                                            attr='symbol',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='cost_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='fifo', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='fifo_vals', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_change_standard_price',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='new_price', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Helper to create the stock valuation layers and the account moves\n        after an update of standard price.\n\n        :param new_price: new standard price\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='p', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='valuation',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='real_time', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='stock.valuation.layer', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='check_access_rights',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='read', kind=None)],
                                            keywords=[
                                                keyword(
                                                    arg='raise_exception',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="You cannot update the cost of a product in automated valuation as it leads to the creation of a journal entry, for which you don't have the access rights.", kind=None)],
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
                        Assign(
                            targets=[Name(id='svl_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
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
                        For(
                            target=Name(id='product', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='cost_method',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value='average', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='quantity_svl', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='quantity_svl',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[Name(id='quantity_svl', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rounding',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='diff', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='new_price', ctx=Load()),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='standard_price',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='company_id', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='quantity_svl', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='diff', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='company_id', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='is_zero',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='svl_vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='quantity', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='company_id', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Product value manually modified (from %s to %s)', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='standard_price',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='new_price', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Name(id='value', ctx=Load()),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='svl_vals_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='svl_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stock_valuation_layers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.valuation.layer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='svl_vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_accounts', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='product', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='get_product_accounts',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='product', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='am_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='stock_valuation_layer', ctx=Store()),
                            iter=Name(id='stock_valuation_layers', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='stock_valuation_layer', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='stock_valuation_layer', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='product', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='valuation',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='real_time', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='product_accounts', ctx=Load()),
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
                                            args=[Constant(value='expense', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You must set a counterpart account on your product category.', kind=None)],
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
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='product_accounts', ctx=Load()),
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
                                            args=[Constant(value='stock_valuation', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="You don't have any stock valuation account defined on your product category. You must define one before processing this operation.", kind=None)],
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
                                If(
                                    test=Compare(
                                        left=Name(id='value', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='debit_account_id', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='product_accounts', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='expense', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='credit_account_id', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='product_accounts', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='stock_valuation', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='debit_account_id', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='product_accounts', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='stock_valuation', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='credit_account_id', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='product_accounts', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='expense', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='move_vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='ref', kind=None),
                                            Constant(value='stock_valuation_layer_ids', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='product_accounts', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='stock_journal', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company_id', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='default_code',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=None, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='stock_valuation_layer', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='entry', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='%(user)s changed cost from %(previous)s to %(new_price)s - %(product)s', kind=None)],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='user',
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='env',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='user',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='previous',
                                                                                value=Attribute(
                                                                                    value=Name(id='product', ctx=Load()),
                                                                                    attr='standard_price',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='new_price',
                                                                                value=Name(id='new_price', ctx=Load()),
                                                                            ),
                                                                            keyword(
                                                                                arg='product',
                                                                                value=Attribute(
                                                                                    value=Name(id='product', ctx=Load()),
                                                                                    attr='display_name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Name(id='debit_account_id', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='abs', ctx=Load()),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value=0, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='%(user)s changed cost from %(previous)s to %(new_price)s - %(product)s', kind=None)],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='user',
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='env',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='user',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='previous',
                                                                                value=Attribute(
                                                                                    value=Name(id='product', ctx=Load()),
                                                                                    attr='standard_price',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='new_price',
                                                                                value=Name(id='new_price', ctx=Load()),
                                                                            ),
                                                                            keyword(
                                                                                arg='product',
                                                                                value=Attribute(
                                                                                    value=Name(id='product', ctx=Load()),
                                                                                    attr='display_name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Name(id='credit_account_id', ctx=Load()),
                                                                    Constant(value=0, kind=None),
                                                                    Call(
                                                                        func=Name(id='abs', ctx=Load()),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='am_vals_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='move_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='account_moves', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='am_vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='account_moves', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='account_moves', ctx=Load()),
                                            attr='_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_run_fifo',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='quantity', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='qty_to_take_on_candidates', ctx=Store())],
                            value=Name(id='quantity', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='candidates', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.valuation.layer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='remaining_qty', kind=None),
                                                    Constant(value='>', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
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
                        Assign(
                            targets=[Name(id='new_standard_price', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tmp_value', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='candidate', ctx=Store()),
                            iter=Name(id='candidates', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='qty_taken_on_candidate', ctx=Store())],
                                    value=Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Name(id='qty_to_take_on_candidates', ctx=Load()),
                                            Attribute(
                                                value=Name(id='candidate', ctx=Load()),
                                                attr='remaining_qty',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='candidate_unit_cost', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='candidate', ctx=Load()),
                                            attr='remaining_value',
                                            ctx=Load(),
                                        ),
                                        op=Div(),
                                        right=Attribute(
                                            value=Name(id='candidate', ctx=Load()),
                                            attr='remaining_qty',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_standard_price', ctx=Store())],
                                    value=Name(id='candidate_unit_cost', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value_taken_on_candidate', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='qty_taken_on_candidate', ctx=Load()),
                                        op=Mult(),
                                        right=Name(id='candidate_unit_cost', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value_taken_on_candidate', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='candidate', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value_taken_on_candidate', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_remaining_value', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='candidate', ctx=Load()),
                                            attr='remaining_value',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Name(id='value_taken_on_candidate', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='candidate_vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='remaining_qty', kind=None),
                                            Constant(value='remaining_value', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='candidate', ctx=Load()),
                                                    attr='remaining_qty',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Name(id='qty_taken_on_candidate', ctx=Load()),
                                            ),
                                            Name(id='new_remaining_value', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='candidate', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='candidate_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='qty_to_take_on_candidates', ctx=Store()),
                                    op=Sub(),
                                    value=Name(id='qty_taken_on_candidate', ctx=Load()),
                                ),
                                AugAssign(
                                    target=Name(id='tmp_value', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='value_taken_on_candidate', ctx=Load()),
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[Name(id='qty_to_take_on_candidates', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rounding',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='remaining_qty',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='rounding',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='next_candidates', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='candidates', ctx=Load()),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='svl', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='svl', ctx=Load()),
                                                                        attr='remaining_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Gt()],
                                                                    comparators=[Constant(value=0, kind=None)],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='new_standard_price', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='next_candidates', ctx=Load()),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='next_candidates', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='unit_cost',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='new_standard_price', ctx=Load()),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Break(),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='new_standard_price', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='cost_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='fifo', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='with_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='company', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='disable_auto_svl',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='standard_price',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='new_standard_price', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='float_is_zero', ctx=Load()),
                                args=[Name(id='qty_to_take_on_candidates', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                            attr='rounding',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='unit_cost', kind=None),
                                        ],
                                        values=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Name(id='tmp_value', ctx=Load()),
                                            ),
                                            BinOp(
                                                left=Name(id='tmp_value', ctx=Load()),
                                                op=Div(),
                                                right=Name(id='quantity', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assert(
                                    test=Compare(
                                        left=Name(id='qty_to_take_on_candidates', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    msg=None,
                                ),
                                Assign(
                                    targets=[Name(id='last_fifo_price', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='new_standard_price', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='standard_price',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='negative_stock_value', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='last_fifo_price', ctx=Load()),
                                        op=Mult(),
                                        right=UnaryOp(
                                            op=USub(),
                                            operand=Name(id='qty_to_take_on_candidates', ctx=Load()),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='tmp_value', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Name(id='abs', ctx=Load()),
                                        args=[Name(id='negative_stock_value', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='remaining_qty', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='unit_cost', kind=None),
                                        ],
                                        values=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Name(id='qty_to_take_on_candidates', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Name(id='tmp_value', ctx=Load()),
                                            ),
                                            Name(id='last_fifo_price', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_run_fifo_vacuum',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compensate layer valued at an estimated price with the price of future receipts\n        if any. If the estimated price is equals to the real price, no layer is created but\n        the original layer is marked as compensated.\n\n        :param company: recordset of `res.company` to limit the execution of the vacuum\n        ', kind=None),
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
                        If(
                            test=Compare(
                                left=Name(id='company', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
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
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='svls_to_vacuum', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.valuation.layer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='remaining_qty', kind=None),
                                                    Constant(value='<', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='stock_move_id', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='create_date, id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='svls_to_vacuum', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='as_svls', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='remaining_qty', kind=None),
                                            Constant(value='>', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='create_date', kind=None),
                                            Constant(value='>=', kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='svls_to_vacuum', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_date',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='all_candidates', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.valuation.layer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='svl_to_vacuum', ctx=Store()),
                            iter=Name(id='svls_to_vacuum', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='candidates', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='all_candidates', ctx=Load()),
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
                                                body=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='create_date',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Gt()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Name(id='svl_to_vacuum', ctx=Load()),
                                                                    attr='create_date',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='r', ctx=Load()),
                                                                        attr='create_date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='svl_to_vacuum', ctx=Load()),
                                                                            attr='create_date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='r', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Gt()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='svl_to_vacuum', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='candidates', ctx=Load()),
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='qty_to_take_on_candidates', ctx=Store())],
                                    value=Call(
                                        func=Name(id='abs', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='svl_to_vacuum', ctx=Load()),
                                                attr='remaining_qty',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='qty_taken_on_candidates', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tmp_value', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='candidate', ctx=Store()),
                                    iter=Name(id='candidates', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty_taken_on_candidate', ctx=Store())],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='remaining_qty',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='qty_to_take_on_candidates', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='qty_taken_on_candidates', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='qty_taken_on_candidate', ctx=Load()),
                                        ),
                                        Assign(
                                            targets=[Name(id='candidate_unit_cost', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='candidate', ctx=Load()),
                                                    attr='remaining_value',
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Attribute(
                                                    value=Name(id='candidate', ctx=Load()),
                                                    attr='remaining_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='value_taken_on_candidate', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='qty_taken_on_candidate', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='candidate_unit_cost', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='value_taken_on_candidate', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='round',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='value_taken_on_candidate', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='new_remaining_value', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='candidate', ctx=Load()),
                                                    attr='remaining_value',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Name(id='value_taken_on_candidate', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='candidate_vals', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='remaining_qty', kind=None),
                                                    Constant(value='remaining_value', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='candidate', ctx=Load()),
                                                            attr='remaining_qty',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Name(id='qty_taken_on_candidate', ctx=Load()),
                                                    ),
                                                    Name(id='new_remaining_value', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='candidate', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='candidate_vals', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Compare(
                                                    left=Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='remaining_qty',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Gt()],
                                                    comparators=[Constant(value=0, kind=None)],
                                                ),
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='all_candidates', ctx=Store()),
                                                    op=Sub(),
                                                    value=Name(id='candidate', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='qty_to_take_on_candidates', ctx=Store()),
                                            op=Sub(),
                                            value=Name(id='qty_taken_on_candidate', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Name(id='tmp_value', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='value_taken_on_candidate', ctx=Load()),
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[Name(id='qty_to_take_on_candidates', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='rounding',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='remaining_value_before_vacuum', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='svl_to_vacuum', ctx=Load()),
                                            attr='unit_cost',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Name(id='qty_taken_on_candidates', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_remaining_qty', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='svl_to_vacuum', ctx=Load()),
                                            attr='remaining_qty',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Name(id='qty_taken_on_candidates', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='corrected_value', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='remaining_value_before_vacuum', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='tmp_value', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='svl_to_vacuum', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='remaining_qty', kind=None)],
                                                values=[Name(id='new_remaining_qty', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='svl_to_vacuum', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='is_zero',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='corrected_value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='corrected_value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='svl_to_vacuum', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='corrected_value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='svl_to_vacuum', ctx=Load()),
                                        attr='stock_move_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='unit_cost', kind=None),
                                            Constant(value='quantity', kind=None),
                                            Constant(value='remaining_qty', kind=None),
                                            Constant(value='stock_move_id', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='stock_valuation_layer_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='corrected_value', ctx=Load()),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='Revaluation of %s (negative inventory)', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='svl_to_vacuum', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='vacuum_svl', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='stock.valuation.layer', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='valuation',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='real_time', kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='as_svls', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Name(id='vacuum_svl', ctx=Load()),
                                                    Name(id='svl_to_vacuum', ctx=Load()),
                                                ],
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
                        Assign(
                            targets=[Name(id='product', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_company',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
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
                                        left=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='cost_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='average', kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='float_is_zero', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='quantity_svl',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='rounding',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='disable_auto_svl',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='standard_price', kind=None)],
                                                values=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='value_svl',
                                                            ctx=Load(),
                                                        ),
                                                        op=Div(),
                                                        right=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='quantity_svl',
                                                            ctx=Load(),
                                                        ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.valuation.layer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='x', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Name(id='as_svls', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_validate_accounting_entries',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='vacuum_svl', ctx=Store()),
                                    Name(id='svl_to_vacuum', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='as_svls', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_create_fifo_vacuum_anglo_saxon_expense_entry',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='vacuum_svl', ctx=Load()),
                                            Name(id='svl_to_vacuum', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_fifo_vacuum_anglo_saxon_expense_entry',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vacuum_svl', annotation=None, type_comment=None),
                            arg(arg='svl_to_vacuum', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" When product is delivered and invoiced while you don't have units in stock anymore, there are chances of that\n            product getting undervalued/overvalued. So, we should nevertheless take into account the fact that the product has\n            already been delivered and invoiced to the customer by posting the value difference in the expense account also.\n            Consider the below case where product is getting undervalued:\n\n            You bought 8 units @ 10$ -> You have a stock valuation of 8 units, unit cost 10.\n            Then you deliver 10 units of the product.\n            You assumed the missing 2 should go out at a value of 10$ but you are not sure yet as it hasn't been bought in Odoo yet.\n            Afterwards, you buy missing 2 units of the same product at 12$ instead of expected 10$.\n            In case the product has been undervalued when delivered without stock, the vacuum entry is the following one (this entry already takes place):\n\n            Account                         | Debit   | Credit\n            ===================================================\n            Stock Valuation                 | 0.00     | 4.00\n            Stock Interim (Delivered)       | 4.00     | 0.00\n\n            So, on delivering product with different price, We should create additional journal items like:\n            Account                         | Debit    | Credit\n            ===================================================\n            Stock Interim (Delivered)       | 0.00     | 4.00\n            Expenses Revaluation            | 4.00     | 0.00\n        ", kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='vacuum_svl', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='anglo_saxon_accounting',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='svl_to_vacuum', ctx=Load()),
                                                    attr='stock_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_is_out',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='AccountMove', ctx=Store())],
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
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='account_move_lines', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='svl_to_vacuum', ctx=Load()),
                                    attr='account_move_id',
                                    ctx=Load(),
                                ),
                                attr='line_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reconciled_line_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='account_move_lines', ctx=Load()),
                                                        attr='_reconciled_lines',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='account_move_lines', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
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
                            targets=[Name(id='account_move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='AccountMove', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='line_ids', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='reconciled_line_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='account_move', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='accounts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='svl_to_vacuum', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='product_tmpl_id',
                                        ctx=Load(),
                                    ),
                                    attr='get_product_accounts',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fiscal_pos',
                                        value=Attribute(
                                            value=Name(id='account_move', ctx=Load()),
                                            attr='fiscal_position_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='accounts', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='stock_output', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='accounts', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='expense', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='description', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Expenses %s', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='vacuum_svl', ctx=Load()),
                                    attr='description',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='vacuum_svl', ctx=Load()),
                                        attr='stock_move_id',
                                        ctx=Load(),
                                    ),
                                    attr='_prepare_account_move_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='vacuum_svl', ctx=Load()),
                                        attr='quantity',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='vacuum_svl', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='accounts', ctx=Load()),
                                            slice=Constant(value='stock_output', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='accounts', ctx=Load()),
                                            slice=Constant(value='expense', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='description', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_account_move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='AccountMove', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='line_ids', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='ref', kind=None),
                                            Constant(value='stock_move_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='accounts', ctx=Load()),
                                                    slice=Constant(value='stock_journal', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='move_lines', ctx=Load()),
                                            Call(
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
                                                    Constant(value='force_period_date', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='context_today',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='self', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='description', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='vacuum_svl', ctx=Load()),
                                                    attr='stock_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='entry', kind=None),
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
                                    value=Name(id='new_account_move', ctx=Load()),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='to_reconcile_account_move_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='vacuum_svl', ctx=Load()),
                                            attr='account_move_id',
                                            ctx=Load(),
                                        ),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='reconciled',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='account_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Name(id='accounts', ctx=Load()),
                                                            slice=Constant(value='stock_output', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='account_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='reconcile',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='to_reconcile_account_move_lines', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='new_account_move', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='reconciled',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='account_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Name(id='accounts', ctx=Load()),
                                                            slice=Constant(value='stock_output', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='account_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='reconcile',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='to_reconcile_account_move_lines', ctx=Load()),
                                    attr='reconcile',
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
                FunctionDef(
                    name='_svl_empty_stock',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='description', annotation=None, type_comment=None),
                            arg(arg='product_category', annotation=None, type_comment=None),
                            arg(arg='product_template', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='impacted_product_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='impacted_products', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.product', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='products_orig_quantity_svl', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='type', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='product', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='product_category', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='categ_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='product_category', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='product_template', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='domain', ctx=Store()),
                                            op=Add(),
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='product_tmpl_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='product_template', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='products', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[Constant(value='quantity_svl', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='product', ctx=Store()),
                            iter=Name(id='products', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='impacted_product_ids', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='product', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='products_orig_quantity_svl', ctx=Load()),
                                            slice=Subscript(
                                                value=Name(id='product', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='product', ctx=Load()),
                                        slice=Constant(value='quantity_svl', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='impacted_products', ctx=Store()),
                            op=BitOr(),
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='impacted_product_ids', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='empty_stock_svl_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='product', ctx=Store()),
                            iter=Name(id='impacted_products', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='quantity_svl',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rounding',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='svsl_vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='_prepare_out_svl_vals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='quantity_svl',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='svsl_vals', ctx=Load()),
                                            slice=Constant(value='description', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Name(id='description', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='svsl_vals', ctx=Load()),
                                                attr='pop',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='rounding_adjustment', kind=None),
                                                Constant(value='', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='svsl_vals', ctx=Load()),
                                            slice=Constant(value='company_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='empty_stock_svl_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='svsl_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='empty_stock_svl_list', ctx=Load()),
                                    Name(id='products_orig_quantity_svl', ctx=Load()),
                                    Name(id='impacted_products', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
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
                    name='_svl_replenish_stock',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='description', annotation=None, type_comment=None),
                            arg(arg='products_orig_quantity_svl', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='refill_stock_svl_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='product', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='quantity_svl', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='products_orig_quantity_svl', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='quantity_svl', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='svl_vals', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='_prepare_in_svl_vals',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='quantity_svl', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='standard_price',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='svl_vals', ctx=Load()),
                                                    slice=Constant(value='description', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='description', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='svl_vals', ctx=Load()),
                                                    slice=Constant(value='company_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='refill_stock_svl_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='svl_vals', ctx=Load())],
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
                            value=Name(id='refill_stock_svl_list', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_svl_empty_stock_am',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stock_valuation_layers', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='move_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_accounts', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='product', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='get_product_accounts',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='product', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='stock_valuation_layers', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='product_id', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='out_stock_valuation_layer', ctx=Store()),
                            iter=Name(id='stock_valuation_layers', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='stock_input_account', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='product_accounts', ctx=Load()),
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
                                        args=[Constant(value='stock_input', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='stock_input_account', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="You don't have any stock input account defined on your product category. You must define one before processing this operation.", kind=None)],
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
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='product_accounts', ctx=Load()),
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
                                            args=[Constant(value='stock_valuation', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="You don't have any stock valuation account defined on your product category. You must define one before processing this operation.", kind=None)],
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
                                Assign(
                                    targets=[Name(id='debit_account_id', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='stock_input_account', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='credit_account_id', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='product_accounts', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='stock_valuation', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move_vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='ref', kind=None),
                                            Constant(value='stock_valuation_layer_ids', kind=None),
                                            Constant(value='line_ids', kind=None),
                                            Constant(value='move_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='product_accounts', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='stock_journal', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='default_code',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=None, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                                                        attr='description',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='debit_account_id', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='abs', ctx=Load()),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value=0, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                                                        attr='description',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='credit_account_id', ctx=Load()),
                                                                    Constant(value=0, kind=None),
                                                                    Call(
                                                                        func=Name(id='abs', ctx=Load()),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='entry', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move_vals_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='move_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='move_vals_list', ctx=Load()),
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
                    name='_svl_replenish_stock_am',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stock_valuation_layers', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='move_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_accounts', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='product', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='get_product_accounts',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='product', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='stock_valuation_layers', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='product_id', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='out_stock_valuation_layer', ctx=Store()),
                            iter=Name(id='stock_valuation_layers', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='product_accounts', ctx=Load()),
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
                                            args=[Constant(value='stock_input', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="You don't have any input valuation account defined on your product category. You must define one before processing this operation.", kind=None)],
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
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='product_accounts', ctx=Load()),
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
                                            args=[Constant(value='stock_valuation', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="You don't have any stock valuation account defined on your product category. You must define one before processing this operation.", kind=None)],
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
                                Assign(
                                    targets=[Name(id='debit_account_id', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='product_accounts', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='stock_valuation', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='credit_account_id', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='product_accounts', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='stock_input', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move_vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='ref', kind=None),
                                            Constant(value='stock_valuation_layer_ids', kind=None),
                                            Constant(value='line_ids', kind=None),
                                            Constant(value='move_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='product_accounts', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='stock_journal', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='default_code',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=None, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                                                        attr='description',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='debit_account_id', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='abs', ctx=Load()),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value=0, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='out_stock_valuation_layer', ctx=Load()),
                                                                        attr='description',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='credit_account_id', ctx=Load()),
                                                                    Constant(value=0, kind=None),
                                                                    Call(
                                                                        func=Name(id='abs', ctx=Load()),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='entry', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move_vals_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='move_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='move_vals_list', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_stock_account_get_anglo_saxon_price_unit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='uom', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='price', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='standard_price',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='self', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='uom', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='uom', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='price', ctx=Load()),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='uom_id',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_price',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='price', ctx=Load()),
                                    Name(id='uom', ctx=Load()),
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
                    name='_compute_average_price',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='qty_invoiced', annotation=None, type_comment=None),
                            arg(arg='qty_to_invoice', annotation=None, type_comment=None),
                            arg(arg='stock_moves', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Go over the valuation layers of `stock_moves` to value `qty_to_invoice` while taking\n        care of ignoring `qty_invoiced`. If `qty_to_invoice` is greater than what's possible to\n        value with the valuation layers, use the product's standard price.\n\n        :param qty_invoiced: quantity already invoiced\n        :param qty_to_invoice: quantity to invoice\n        :param stock_moves: recordset of `stock.move`\n        :returns: the anglo saxon price unit\n        :rtype: float\n        ", kind=None),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='qty_to_invoice', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=0, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='returned_quantities', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='float', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='stock_moves', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='origin_returned_move_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='returned_quantities', ctx=Load()),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='origin_returned_move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='abs', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='sum', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='move', ctx=Load()),
                                                                                attr='sudo',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='stock_valuation_layer_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='mapped',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='quantity', kind=None)],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='candidates', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='stock_moves', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=UnaryOp(
                                                            op=Not(),
                                                            operand=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='m', ctx=Load()),
                                                                        attr='origin_returned_move_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Compare(
                                                                        left=Call(
                                                                            func=Name(id='sum', ctx=Load()),
                                                                            args=[
                                                                                Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='m', ctx=Load()),
                                                                                            attr='stock_valuation_layer_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='mapped',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='quantity', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[GtE()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='stock_valuation_layer_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='qty_to_take_on_candidates', ctx=Store())],
                            value=Name(id='qty_to_invoice', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tmp_value', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='candidate', ctx=Store()),
                            iter=Name(id='candidates', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='candidate', ctx=Load()),
                                            attr='quantity',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='candidate_quantity', ctx=Store())],
                                    value=Call(
                                        func=Name(id='abs', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='candidate', ctx=Load()),
                                                attr='quantity',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='candidate', ctx=Load()),
                                                attr='stock_move_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='returned_quantities', ctx=Load())],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='candidate_quantity', ctx=Store()),
                                            op=Sub(),
                                            value=Subscript(
                                                value=Name(id='returned_quantities', ctx=Load()),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='stock_move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[Name(id='candidate_quantity', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rounding',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='float_is_zero', ctx=Load()),
                                            args=[Name(id='qty_invoiced', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='candidate', ctx=Load()),
                                                            attr='uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='rounding',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty_ignored', ctx=Store())],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Name(id='qty_invoiced', ctx=Load()),
                                                    Name(id='candidate_quantity', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='qty_invoiced', ctx=Store()),
                                            op=Sub(),
                                            value=Name(id='qty_ignored', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Name(id='candidate_quantity', ctx=Store()),
                                            op=Sub(),
                                            value=Name(id='qty_ignored', ctx=Load()),
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[Name(id='candidate_quantity', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='candidate', ctx=Load()),
                                                                attr='uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='rounding',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='qty_taken_on_candidate', ctx=Store())],
                                    value=Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Name(id='qty_to_take_on_candidates', ctx=Load()),
                                            Name(id='candidate_quantity', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='qty_to_take_on_candidates', ctx=Store()),
                                    op=Sub(),
                                    value=Name(id='qty_taken_on_candidate', ctx=Load()),
                                ),
                                AugAssign(
                                    target=Name(id='tmp_value', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Name(id='qty_taken_on_candidate', ctx=Load()),
                                        op=Mult(),
                                        right=BinOp(
                                            left=BinOp(
                                                left=Attribute(
                                                    value=Name(id='candidate', ctx=Load()),
                                                    attr='value',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='sum', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='candidate', ctx=Load()),
                                                                    attr='stock_valuation_layer_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='value', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            op=Div(),
                                            right=Attribute(
                                                value=Name(id='candidate', ctx=Load()),
                                                attr='quantity',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[Name(id='qty_to_take_on_candidates', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rounding',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='float_is_zero', ctx=Load()),
                                    args=[Name(id='qty_to_take_on_candidates', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='precision_rounding',
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='rounding',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='negative_stock_value', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='standard_price',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Name(id='qty_to_take_on_candidates', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='tmp_value', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='negative_stock_value', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='tmp_value', ctx=Load()),
                                op=Div(),
                                right=Name(id='qty_to_invoice', ctx=Load()),
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
                    targets=[Name(id='property_valuation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='manual_periodic', kind=None),
                                            Constant(value='Manual', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='real_time', kind=None),
                                            Constant(value='Automated', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Inventory Valuation', kind=None),
                            ),
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Manual: The accounting entries to value the inventory are not posted automatically.\n        Automated: An accounting entry is automatically created to value the inventory when a product enters or leaves the company.\n        ', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_cost_method', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='standard', kind=None),
                                            Constant(value='Standard Price', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='fifo', kind=None),
                                            Constant(value='First In First Out (FIFO)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='average', kind=None),
                                            Constant(value='Average Cost (AVCO)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Costing Method', kind=None),
                            ),
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Standard Price: The products are valued at their standard cost defined on the product.\n        Average Cost (AVCO): The products are valued at weighted average cost.\n        First In First Out (FIFO): The products are valued supposing those that enter the company first will also leave it first.\n        ', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_stock_journal', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.journal', kind=None),
                            Constant(value='Stock Journal', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', '=', allowed_company_ids[0])]", kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When doing automated inventory valuation, this is the Accounting Journal in which entries will be automatically posted when stock moves are processed.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_stock_account_input_categ_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.account', kind=None),
                            Constant(value='Stock Input Account', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', '=', allowed_company_ids[0]), ('deprecated', '=', False)]", kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Counterpart journal items for all incoming stock moves will be posted in this account, unless there is a specific valuation account\n                set on the source location. This is the default value for all products in this category. It can also directly be set on each product.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_stock_account_output_categ_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.account', kind=None),
                            Constant(value='Stock Output Account', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', '=', allowed_company_ids[0]), ('deprecated', '=', False)]", kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When doing automated inventory valuation, counterpart journal items for all outgoing stock moves will be posted in this account,\n                unless there is a specific valuation account set on the destination location. This is the default value for all products in this category.\n                It can also directly be set on each product.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_stock_valuation_account_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.account', kind=None),
                            Constant(value='Stock Valuation Account', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', '=', allowed_company_ids[0]), ('deprecated', '=', False)]", kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When automated inventory valuation is enabled on a product, this account will hold the current value of the products.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_valuation_accouts',
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
                            target=Name(id='category', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='valuation_account', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='category', ctx=Load()),
                                        attr='property_stock_valuation_account_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='input_and_output_accounts', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='category', ctx=Load()),
                                            attr='property_stock_account_input_categ_id',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='category', ctx=Load()),
                                            attr='property_stock_account_output_categ_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='valuation_account', ctx=Load()),
                                            Compare(
                                                left=Name(id='valuation_account', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='input_and_output_accounts', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The Stock Input and/or Output accounts cannot be the same as the Stock Valuation account.', kind=None)],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='property_stock_valuation_account_id', kind=None),
                                Constant(value='property_stock_account_output_categ_id', kind=None),
                                Constant(value='property_stock_account_input_categ_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='onchange_property_valuation',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_origin',
                                    ctx=Load(),
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
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
                                                args=[Constant(value='Warning', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Changing your cost method is an important change that will impact your inventory valuation. Are you sure you want to make that change?', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='property_cost_method', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='impacted_categories', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Product', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.product', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='SVL', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.valuation.layer', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='property_cost_method', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='property_valuation', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_cost_method', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='property_cost_method', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_valuation', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='property_valuation', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='product_category', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='valuation_impacted', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='new_cost_method', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='new_cost_method', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='product_category', ctx=Load()),
                                                                attr='property_cost_method',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='valuation_impacted', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='new_valuation', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='new_valuation', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='product_category', ctx=Load()),
                                                                attr='property_valuation',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='valuation_impacted', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='valuation_impacted', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='new_cost_method', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='description', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Costing method change for product category %s: from %s to %s.', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='product_category', ctx=Load()),
                                                                    attr='display_name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='product_category', ctx=Load()),
                                                                    attr='property_cost_method',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='new_cost_method', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='description', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Valuation method change for product category %s: from %s to %s.', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='product_category', ctx=Load()),
                                                                    attr='display_name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='product_category', ctx=Load()),
                                                                    attr='property_valuation',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='new_valuation', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='out_svl_vals_list', ctx=Store()),
                                                        Name(id='products_orig_quantity_svl', ctx=Store()),
                                                        Name(id='products', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Product', ctx=Load()),
                                                    attr='_svl_empty_stock',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='description', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='product_category',
                                                        value=Name(id='product_category', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='out_stock_valuation_layers', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='SVL', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='out_svl_vals_list', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='product_category', ctx=Load()),
                                                    attr='property_valuation',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='real_time', kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='move_vals_list', ctx=Store()),
                                                    op=Add(),
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Product', ctx=Load()),
                                                            attr='_svl_empty_stock_am',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='out_stock_valuation_layers', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='impacted_categories', ctx=Load()),
                                                    slice=Name(id='product_category', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='products', ctx=Load()),
                                                    Name(id='description', ctx=Load()),
                                                    Name(id='products_orig_quantity_svl', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProductCategory', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='product_category', ctx=Store()),
                                    Tuple(
                                        elts=[
                                            Name(id='products', ctx=Store()),
                                            Name(id='description', ctx=Store()),
                                            Name(id='products_orig_quantity_svl', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='impacted_categories', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='in_svl_vals_list', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='products', ctx=Load()),
                                            attr='_svl_replenish_stock',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='description', ctx=Load()),
                                            Name(id='products_orig_quantity_svl', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='in_stock_valuation_layers', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='SVL', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='in_svl_vals_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='product_category', ctx=Load()),
                                            attr='property_valuation',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='real_time', kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='move_vals_list', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Product', ctx=Load()),
                                                    attr='_svl_replenish_stock_am',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='in_stock_valuation_layers', ctx=Load())],
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='move_vals_list', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='stock.valuation.layer', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='check_access_rights',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='read', kind=None)],
                                            keywords=[
                                                keyword(
                                                    arg='raise_exception',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="The action leads to the creation of a journal entry, for which you don't have the access rights.", kind=None)],
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
                        If(
                            test=Name(id='move_vals_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='account_moves', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='move_vals_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='account_moves', ctx=Load()),
                                            attr='_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
