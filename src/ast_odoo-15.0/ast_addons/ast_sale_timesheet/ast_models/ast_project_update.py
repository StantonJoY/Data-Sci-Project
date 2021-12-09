Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_utils', asname=None),
                alias(name='format_amount', asname=None),
                alias(name='formatLang', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ProjectUpdate',
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
                    value=Constant(value='project.update', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_template_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='project', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='template_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProjectUpdate', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_template_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='project', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='services', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_services_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='project', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profitability', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_profitability_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='project', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='show_sold', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='template_values', ctx=Load()),
                                            slice=Constant(value='project', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='allow_billable',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='services', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='data', kind=None),
                                                        List(elts=[], ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    None,
                                    Constant(value='show_sold', kind=None),
                                    Constant(value='show_profitability', kind=None),
                                    Constant(value='show_activities', kind=None),
                                    Constant(value='services', kind=None),
                                    Constant(value='profitability', kind=None),
                                ],
                                values=[
                                    Name(id='template_values', ctx=Load()),
                                    Name(id='show_sold', ctx=Load()),
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='profitability', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='template_values', ctx=Load()),
                                                slice=Constant(value='show_activities', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='show_sold', ctx=Load()),
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[Name(id='profitability', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Name(id='services', ctx=Load()),
                                    Name(id='profitability', ctx=Load()),
                                ],
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
                    name='_get_project_sols',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='project', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Return(value=None)],
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
                    name='_get_services_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='project', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='project', ctx=Load()),
                                    attr='allow_billable',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='services', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='total_sold', ctx=Store()),
                                        Name(id='total_effective', ctx=Store()),
                                        Name(id='total_remaining', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sols', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='project', ctx=Load()),
                                    attr='_get_sale_order_lines',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name_by_sol', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='sols', ctx=Load()),
                                            attr='name_get',
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
                            targets=[Name(id='product_uom_unit', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='sol', ctx=Store()),
                            iter=Name(id='sols', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='is_unit', ctx=Store())],
                                    value=Compare(
                                        left=Attribute(
                                            value=Name(id='sol', ctx=Load()),
                                            attr='product_uom',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='product_uom_unit', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sol', ctx=Load()),
                                                        attr='product_uom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='category_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
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
                                                            attr='timesheet_encode_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='category_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Name(id='is_unit', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='product_uom_qty', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sol', ctx=Load()),
                                                        attr='product_uom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='sol', ctx=Load()),
                                                        attr='product_uom_qty',
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
                                                        attr='timesheet_encode_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='raise_if_failure',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='qty_delivered', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sol', ctx=Load()),
                                                        attr='product_uom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='sol', ctx=Load()),
                                                        attr='qty_delivered',
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
                                                        attr='timesheet_encode_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='raise_if_failure',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='services', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='sold_value', kind=None),
                                                            Constant(value='effective_value', kind=None),
                                                            Constant(value='remaining_value', kind=None),
                                                            Constant(value='unit', kind=None),
                                                            Constant(value='is_unit', kind=None),
                                                            Constant(value='sol', kind=None),
                                                        ],
                                                        values=[
                                                            IfExp(
                                                                test=Compare(
                                                                    left=Call(
                                                                        func=Name(id='len', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='sols', ctx=Load()),
                                                                                attr='order_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    ops=[Gt()],
                                                                    comparators=[Constant(value=1, kind=None)],
                                                                ),
                                                                body=Subscript(
                                                                    value=Name(id='name_by_sol', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='sol', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                orelse=Attribute(
                                                                    value=Name(id='sol', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Name(id='product_uom_qty', ctx=Load()),
                                                            Name(id='qty_delivered', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='product_uom_qty', ctx=Load()),
                                                                op=Sub(),
                                                                right=Name(id='qty_delivered', ctx=Load()),
                                                            ),
                                                            IfExp(
                                                                test=Name(id='is_unit', ctx=Load()),
                                                                body=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='sol', ctx=Load()),
                                                                        attr='product_uom',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                orelse=Attribute(
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
                                                                        attr='timesheet_encode_uom_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Name(id='is_unit', ctx=Load()),
                                                            Name(id='sol', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sol', ctx=Load()),
                                                        attr='product_uom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='category_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
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
                                                            attr='timesheet_encode_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='category_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='total_sold', ctx=Store()),
                                                    op=Add(),
                                                    value=Name(id='product_uom_qty', ctx=Load()),
                                                ),
                                                AugAssign(
                                                    target=Name(id='total_effective', ctx=Store()),
                                                    op=Add(),
                                                    value=Name(id='qty_delivered', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total_remaining', ctx=Store())],
                            value=BinOp(
                                left=Name(id='total_sold', ctx=Load()),
                                op=Sub(),
                                right=Name(id='total_effective', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='data', kind=None),
                                    Constant(value='total_sold', kind=None),
                                    Constant(value='total_effective', kind=None),
                                    Constant(value='total_remaining', kind=None),
                                    Constant(value='company_unit_name', kind=None),
                                ],
                                values=[
                                    Name(id='services', ctx=Load()),
                                    Name(id='total_sold', ctx=Load()),
                                    Name(id='total_effective', ctx=Load()),
                                    Name(id='total_remaining', ctx=Load()),
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
                                            attr='timesheet_encode_uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
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
                    name='_get_profitability_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='project', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='costs_revenues', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='analytic_account_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='allow_billable',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_has_groups',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='project.group_project_manager', kind=None)],
                                            keywords=[],
                                        ),
                                        Name(id='costs_revenues', ctx=Load()),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='profitability', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='project', ctx=Load()),
                                    attr='_get_profitability_common',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='analytic_account_id', kind=None),
                                    Constant(value='costs', kind=None),
                                    Constant(value='revenues', kind=None),
                                    Constant(value='margin', kind=None),
                                    Constant(value='margin_formatted', kind=None),
                                    Constant(value='margin_percentage', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='analytic_account_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='format_amount', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Subscript(
                                                    value=Name(id='profitability', ctx=Load()),
                                                    slice=Constant(value='costs', kind=None),
                                                    ctx=Load(),
                                                ),
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
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='format_amount', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='profitability', ctx=Load()),
                                                slice=Constant(value='revenues', kind=None),
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
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='profitability', ctx=Load()),
                                        slice=Constant(value='margin', kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='format_amount', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='profitability', ctx=Load()),
                                                slice=Constant(value='margin', kind=None),
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
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='formatLang', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='float_utils', ctx=Load()),
                                                                        attr='float_is_zero',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='profitability', ctx=Load()),
                                                                            slice=Constant(value='costs', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='precision_digits',
                                                                            value=Constant(value=2, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            BinOp(
                                                                left=UnaryOp(
                                                                    op=USub(),
                                                                    operand=BinOp(
                                                                        left=Subscript(
                                                                            value=Name(id='profitability', ctx=Load()),
                                                                            slice=Constant(value='margin', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Div(),
                                                                        right=Subscript(
                                                                            value=Name(id='profitability', ctx=Load()),
                                                                            slice=Constant(value='costs', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ),
                                                                op=Mult(),
                                                                right=Constant(value=100, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='digits',
                                                value=Constant(value=0, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
