Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='AccountTaxReportLine',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='account.tax.report.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='carry_over_condition_method', ctx=Store())],
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
                                                Constant(value='vp14_debt_carryover_condition', kind=None),
                                                Constant(value='Italian line vp14 debt carryover', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='vp14_credit_carryover_condition', kind=None),
                                                Constant(value='Italian line vp14 credit carryover', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='vp14_debt_carryover_condition',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='line_amount', annotation=None, type_comment=None),
                            arg(arg='carried_over_amount', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        The vp14 debt line will be carried over to the vp7 line of the next period, if the amount is between 0 and 25.82\n        Else the amount in vp7 will stay 0\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='tax_unit', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='company_only', kind=None)],
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
                            orelse=[
                                Assign(
                                    targets=[Name(id='tax_unit', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax.unit', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='tax_unit', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='tax_unit', ctx=Load()),
                                        attr='main_company_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='base_currency', ctx=Store())],
                            value=Attribute(
                                value=Name(id='company', ctx=Load()),
                                attr='currency_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='target_currency', ctx=Store())],
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
                            targets=[Name(id='amount_in_euro', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base_currency', ctx=Load()),
                                    attr='_convert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='line_amount', ctx=Load()),
                                    Name(id='target_currency', ctx=Load()),
                                    Name(id='company', ctx=Load()),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='date', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='date_to', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='amount_in_euro', ctx=Load()),
                                ops=[LtE()],
                                comparators=[Constant(value=25.82, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='vp14_credit_carryover_condition',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='line_amount', annotation=None, type_comment=None),
                            arg(arg='carried_over_amount', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        If there is a credit, this amount will be carried over to the vp8 line of the next period.\n        This is only done during the same year.\n        If we are between two years, we want to carry it over to the vp9 line.\n        ', kind=None),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value=None, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_carryover_destination_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
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
                            targets=[Name(id='italian_report_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_xmlid_to_res_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='l10n_it.tax_report_vat', kind=None)],
                                keywords=[],
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
                                                value=Name(id='self', ctx=Load()),
                                                attr='report_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='italian_report_id', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='VP14b', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_get_carryover_destination_line',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='options', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='end_of_period_month', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='fields', ctx=Load()),
                                            attr='Date',
                                            ctx=Load(),
                                        ),
                                        attr='from_string',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='date', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='date_to', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='month',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='end_of_period_month', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=12, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='line', ctx=Store())],
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
                                        args=[Constant(value='l10n_it.tax_report_line_vp9', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='line', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='carry_over_destination_line_id',
                                                ctx=Load(),
                                            ),
                                            Name(id='self', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='line', ctx=Load()),
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
