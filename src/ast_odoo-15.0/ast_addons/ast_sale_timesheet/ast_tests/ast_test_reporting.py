Module(
    body=[
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_is_zero', asname=None),
                alias(name='float_compare', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.sale_timesheet.tests.common_reporting',
            names=[alias(name='TestCommonReporting', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestReporting',
            bases=[Name(id='TestCommonReporting', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_profitability_report',
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
                            targets=[Name(id='rounding', ctx=Store())],
                            value=Attribute(
                                value=Name(id='currency', ctx=Load()),
                                attr='rounding',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_stat', ctx=Store())],
                            value=Subscript(
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
                                                    slice=Constant(value='project.profitability.report', kind=None),
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
                                                                Constant(value='project_id', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='project_global',
                                                                        ctx=Load(),
                                                                    ),
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
                                        attr='read',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet unit amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order_1',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order_2',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order_3',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_1', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_deliver_project',
                                    ctx=Load(),
                                ),
                                attr='project_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_order_project',
                                    ctx=Load(),
                                ),
                                attr='project_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_deliver_manual_project',
                                    ctx=Load(),
                                ),
                                attr='project_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_so_1', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_deliver_project',
                                    ctx=Load(),
                                ),
                                attr='task_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_so_2', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_order_project',
                                    ctx=Load(),
                                ),
                                attr='task_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_so_3', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_deliver_manual_project',
                                    ctx=Load(),
                                ),
                                attr='task_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_in_global_1', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_deliver_task',
                                    ctx=Load(),
                                ),
                                attr='task_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_in_global_2', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_order_task',
                                    ctx=Load(),
                                ),
                                attr='task_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_1', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet unit amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet cost of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty_to_invoice',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice should be the one from the SO line, as we are in ordered quantity', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet unit amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_3', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet unit amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet cost of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_global_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='project_global',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_task',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_task',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty_to_invoice',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value="The amount to invoice of global project should take the task in 'oredered qty' into account", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet unit amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='timesheet1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_1', ctx=Load()),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_2', ctx=Load()),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_1', ctx=Load()),
                                    Constant(value=3, kind=None),
                                    Name(id='task_so_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_2', ctx=Load()),
                                    Constant(value=3, kind=None),
                                    Name(id='task_so_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet5', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_manager',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_1', ctx=Load()),
                                    Constant(value=1, kind=None),
                                    Name(id='task_so_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet6', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_manager',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_2', ctx=Load()),
                                    Constant(value=1, kind=None),
                                    Name(id='task_so_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet7', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_manager',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_global',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
                                    Name(id='task_in_global_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet8', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_manager',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_global',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
                                    Name(id='task_in_global_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet9', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_3', ctx=Load()),
                                    Constant(value=4, kind=None),
                                    Name(id='task_so_3', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_1', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice of the project from SO1 should only include timesheet linked to task', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO1 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO1 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the deliver project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty_to_invoice',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice should be the one from the SO line, as we are in ordered quantity', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_3', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_cost', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_sold_unit', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='unit_amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_global_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='project_global',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_unit', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_to_invoice', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_deliver_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Name(id='timesheet7', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_to_invoice', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value="The amount to invoice of global project should take the task in 'oredered qty' and the delivered timesheets into account", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_deliver_manual_project',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='qty_delivered', kind=None)],
                                        values=[Constant(value=7.0, kind=None)],
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_1', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice of the project from SO1 should only include timesheet linked to task', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO1 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO1 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the deliver project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty_to_invoice',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice should be the one from the SO line, as we are in ordered quantity', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_3', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_cost', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_sold_unit', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='unit_amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_manual_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_manual_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty_to_invoice',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_global_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='project_global',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_unit', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_to_invoice', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_deliver_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Name(id='timesheet7', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_to_invoice', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value="The amount to invoice of global project should take the task in 'oredered qty' and the delivered timesheets into account", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='InvoiceWizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.advance.payment.inv', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='mail_notrack',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                    Constant(value='active_id', kind=None),
                                    Constant(value='open_invoices', kind=None),
                                ],
                                values=[
                                    Constant(value='sale.order', kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order_1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order_1',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='InvoiceWizard', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='advance_payment_method', kind=None)],
                                        values=[Constant(value='delivered', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action_invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='payment', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create_invoices',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_id', ctx=Store())],
                            value=Subscript(
                                value=Name(id='action_invoice', ctx=Load()),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_1', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_1', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_1', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the project from SO1 should only include timesheet linked to task', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO1 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO1 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the deliver project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty_to_invoice',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice should be the one from the SO line, as we are in ordered quantity', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_3', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_cost', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_sold_unit', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='unit_amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_manual_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_manual_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty_to_invoice',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_global_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='project_global',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_unit', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_to_invoice', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_order_task',
                                        ctx=Load(),
                                    ),
                                    attr='price_unit',
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_order_task',
                                        ctx=Load(),
                                    ),
                                    attr='product_uom_qty',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_invoiced', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_deliver_task',
                                        ctx=Load(),
                                    ),
                                    attr='price_unit',
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_invoiced', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_to_invoice', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value="The amount to invoice of global project should take the task in 'oredered qty' and the delivered timesheets into account", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                    Constant(value='active_id', kind=None),
                                    Constant(value='open_invoices', kind=None),
                                ],
                                values=[
                                    Constant(value='sale.order', kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order_2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order_2',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='InvoiceWizard', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='advance_payment_method', kind=None)],
                                        values=[Constant(value='delivered', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action_invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='payment', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create_invoices',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_id', ctx=Store())],
                            value=Subscript(
                                value=Name(id='action_invoice', ctx=Load()),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_2', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_2', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_1', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the project from SO1 should only include timesheet linked to task', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO1 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO1 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the deliver project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_uom_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount should be the one from the SO line, as we are in ordered quantity', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice should be the one 0.0, as all ordered quantity is invoiced', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_3', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_cost', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_sold_unit', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='unit_amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_manual_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_manual_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty_to_invoice',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_global_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='project_global',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_unit', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_invoiced', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_deliver_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Name(id='timesheet7', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_invoiced', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value="The amount to invoice of global project should take the task in 'oredered qty' and the delivered timesheets into account", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                    Constant(value='active_id', kind=None),
                                    Constant(value='open_invoices', kind=None),
                                ],
                                values=[
                                    Constant(value='sale.order', kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order_3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order_3',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='InvoiceWizard', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='advance_payment_method', kind=None)],
                                        values=[Constant(value='delivered', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action_invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='payment', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create_invoices',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_id', ctx=Store())],
                            value=Subscript(
                                value=Name(id='action_invoice', ctx=Load()),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_3', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_3', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_1', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the project from SO1 should only include timesheet linked to task', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO1 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO1 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the deliver project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_uom_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount should be the one from the SO line, as we are in ordered quantity', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice should be the one 0.0, as all ordered quantity is invoiced', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_3', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_cost', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_3_timesheet_sold_unit', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet9', ctx=Load()),
                                attr='unit_amount',
                                ctx=Load(),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_manual_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_manual_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty_delivered',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the project from SO3 should be the delivered quantity * the unit price', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_3_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO3', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_3_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO3 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_global_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='project_global',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_unit', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_invoiced', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_deliver_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Name(id='timesheet7', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_invoiced', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value="The amount to invoice of global project should take the task in 'oredered qty' and the delivered timesheets into account", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='so_line_expense', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='price_unit', kind=None),
                                            Constant(value='order_id', kind=None),
                                            Constant(value='is_expense', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_expense',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_expense',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_expense',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_expense',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order_1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='AnalyticLine', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.analytic.line', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expense1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='AnalyticLine', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='account_id', kind=None),
                                            Constant(value='so_line', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='expense on project_so_1', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='project_so_1', ctx=Load()),
                                                    attr='analytic_account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='so_line_expense', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_user',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4, kind=None),
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=4, kind=None),
                                                    op=Mult(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_expense',
                                                            ctx=Load(),
                                                        ),
                                                        attr='list_price',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Mult(),
                                                right=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_expense',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_expense',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
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
                        Assign(
                            targets=[Name(id='expense2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='AnalyticLine', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='account_id', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='expense on global project', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='project_global',
                                                        ctx=Load(),
                                                    ),
                                                    attr='analytic_account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_user',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=2, kind=None),
                                                    op=Mult(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_expense',
                                                            ctx=Load(),
                                                        ),
                                                        attr='list_price',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Mult(),
                                                right=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_expense',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_expense',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_1', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_1_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet5', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_deliver_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the project from SO1 should only include timesheet linked to task', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO1 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_1_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO1 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='expense1', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The expense cost to reinvoice of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='expense1', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The expense cost of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_1_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the deliver project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='so_line_order_project',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_uom_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount should be the one from the SO line, as we are in ordered quantity', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice should be the one 0.0, as all ordered quantity is invoiced', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_global_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='project_global',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_timesheet_unit', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='timesheet7', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet8', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_global_invoiced', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_order_task',
                                            ctx=Load(),
                                        ),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so_line_deliver_task',
                                            ctx=Load(),
                                        ),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Name(id='timesheet7', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_invoiced', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value="The amount to invoice of global project should take the task in 'oredered qty' and the delivered timesheets into account", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_global_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the global project should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO1 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='expense2', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The expense cost of the global project should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_global_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the global project should be 0.0', kind=None),
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
                    name='test_reversed_downpayment',
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
                            targets=[Name(id='rounding', ctx=Store())],
                            value=Attribute(
                                value=Name(id='currency', ctx=Load()),
                                attr='rounding',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order_2',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                    Constant(value='active_id', kind=None),
                                    Constant(value='default_journal_id', kind=None),
                                    Constant(value='open_invoices', kind=None),
                                ],
                                values=[
                                    Constant(value='sale.order', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order_2',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order_2',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_journal_sale', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='downpayment', ctx=Store())],
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
                                                slice=Constant(value='sale.advance.payment.inv', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='advance_payment_method', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='percentage', kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action_invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='downpayment', ctx=Load()),
                                    attr='create_invoices',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_id', ctx=Store())],
                            value=Subscript(
                                value=Name(id='action_invoice', ctx=Load()),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_downpayment', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_downpayment', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='posted_invoice_res_ids', ctx=Store())],
                            value=List(
                                elts=[Name(id='invoice_id', ctx=Load())],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='downpayment2', ctx=Store())],
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
                                                slice=Constant(value='sale.advance.payment.inv', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='advance_payment_method', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='percentage', kind=None),
                                            Constant(value=25, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action_invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='downpayment2', ctx=Load()),
                                    attr='create_invoices',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_downpayment2', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='action_invoice', ctx=Load()),
                                                        slice=Constant(value='domain', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='not in', kind=None),
                                                                    Name(id='posted_invoice_res_ids', ctx=Load()),
                                                                ],
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_downpayment2', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Name(id='posted_invoice_res_ids', ctx=Store()),
                            op=Add(),
                            value=Attribute(
                                value=Name(id='invoice_downpayment2', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='milestone_to_invoice', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_order_project',
                                        ctx=Load(),
                                    ),
                                    attr='price_unit',
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_order_project',
                                        ctx=Load(),
                                    ),
                                    attr='qty_to_invoice',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheets_to_invoice', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_order_task',
                                        ctx=Load(),
                                    ),
                                    attr='price_unit',
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_order_task',
                                        ctx=Load(),
                                    ),
                                    attr='qty_to_invoice',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total_product_price', ctx=Store())],
                            value=BinOp(
                                left=Name(id='milestone_to_invoice', ctx=Load()),
                                op=Add(),
                                right=Name(id='timesheets_to_invoice', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='credit_note_wizard', ctx=Store())],
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
                                                slice=Constant(value='account.move.reversal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='active_ids', kind=None),
                                                    Constant(value='active_id', kind=None),
                                                    Constant(value='active_model', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='invoice_downpayment2', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='invoice_downpayment2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='account.move', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='refund_method', kind=None),
                                            Constant(value='reason', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='refund', kind=None),
                                            Constant(value='reason test create', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='invoice_downpayment2', ctx=Load()),
                                                    attr='journal_id',
                                                    ctx=Load(),
                                                ),
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
                        Assign(
                            targets=[Name(id='action_moves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='credit_note_wizard', ctx=Load()),
                                    attr='reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='credit_id', ctx=Store())],
                            value=Subscript(
                                value=Name(id='action_moves', ctx=Load()),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_credit', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='credit_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_credit', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Name(id='posted_invoice_res_ids', ctx=Store()),
                            op=Add(),
                            value=Attribute(
                                value=Name(id='invoice_credit', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_order_project',
                                    ctx=Load(),
                                ),
                                attr='project_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_so_2', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_order_project',
                                    ctx=Load(),
                                ),
                                attr='task_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_in_global_2', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_order_task',
                                    ctx=Load(),
                                ),
                                attr='task_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value=0.1, kind=None),
                                                op=Mult(),
                                                right=Name(id='total_product_price', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount is the amount of downpayments not reversed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Name(id='milestone_to_invoice', ctx=Load()),
                                                op=Sub(),
                                                right=BinOp(
                                                    left=Constant(value=0.1, kind=None),
                                                    op=Mult(),
                                                    right=Name(id='total_product_price', ctx=Load()),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice is the milestone product minus the downpayment not reversed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet unit amount of the project from SO2 is 0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet cost of the project from SO2 is 0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='timesheet2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_2', ctx=Load()),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_2', ctx=Load()),
                                    Constant(value=3, kind=None),
                                    Name(id='task_so_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet6', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_manager',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_2', ctx=Load()),
                                    Constant(value=2, kind=None),
                                    Name(id='task_so_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet8', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_manager',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_global',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
                                    Name(id='task_in_global_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='so_line_expense', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='price_unit', kind=None),
                                            Constant(value='order_id', kind=None),
                                            Constant(value='is_expense', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_expense',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_expense',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_expense',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_expense',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order_2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expense1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='account_id', kind=None),
                                            Constant(value='so_line', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='expense on project_so_2', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='project_so_2', ctx=Load()),
                                                    attr='analytic_account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='so_line_expense', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_user',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4, kind=None),
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=4, kind=None),
                                                    op=Mult(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_expense',
                                                            ctx=Load(),
                                                        ),
                                                        attr='list_price',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Mult(),
                                                right=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_expense',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_expense',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='amount',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_sold_unit', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='timesheet2', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='timesheet4', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='timesheet6', ctx=Load()),
                                    attr='unit_amount',
                                    ctx=Load(),
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value=0.1, kind=None),
                                                op=Mult(),
                                                right=Name(id='total_product_price', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the project from SO2 should only include downpayment not reversed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Name(id='milestone_to_invoice', ctx=Load()),
                                                op=Sub(),
                                                right=BinOp(
                                                    left=Constant(value=0.1, kind=None),
                                                    op=Mult(),
                                                    right=Name(id='total_product_price', ctx=Load()),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice of the project from SO2 should include the milestone to invoice minus the downpayment', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Attribute(
                                                    value=Name(id='expense1', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be the expense amount', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='expense1', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The expense cost of the project from SO1 should be expense amount', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                    Constant(value='active_id', kind=None),
                                    Constant(value='open_invoices', kind=None),
                                    Constant(value='mail_notrack', kind=None),
                                ],
                                values=[
                                    Constant(value='sale.order', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order_2',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order_2',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
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
                                                slice=Constant(value='sale.advance.payment.inv', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mail_notrack',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='advance_payment_method', kind=None)],
                                        values=[Constant(value='delivered', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action_invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='payment', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create_invoices',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_payment', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='action_invoice', ctx=Load()),
                                                        slice=Constant(value='domain', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='not in', kind=None),
                                                                    Name(id='posted_invoice_res_ids', ctx=Load()),
                                                                ],
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_payment', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='milestone_to_invoice', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the project from SO2 should only include timesheet linked to task', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense to invoice amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='expense1', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The expense cost reinvoiced of the project from SO2 should be the expense amount', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='expense1', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The expense cost of the project from SO2 should be the expense amount', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='credit_note_wizard', ctx=Store())],
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
                                                slice=Constant(value='account.move.reversal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='active_ids', kind=None),
                                                    Constant(value='active_id', kind=None),
                                                    Constant(value='active_model', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='invoice_payment', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='invoice_payment', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='account.move', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='refund_method', kind=None),
                                            Constant(value='reason', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='refund', kind=None),
                                            Constant(value='reason test create', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='invoice_payment', ctx=Load()),
                                                    attr='journal_id',
                                                    ctx=Load(),
                                                ),
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
                        Assign(
                            targets=[Name(id='action_moves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='credit_note_wizard', ctx=Load()),
                                    attr='reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='credit_id', ctx=Store())],
                            value=Subscript(
                                value=Name(id='action_moves', ctx=Load()),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_credit', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='credit_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_credit', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value=0.1, kind=None),
                                                op=Mult(),
                                                right=Name(id='total_product_price', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the project from SO2 should only include downpayment not reversed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Name(id='milestone_to_invoice', ctx=Load()),
                                                op=Sub(),
                                                right=BinOp(
                                                    left=Constant(value=0.1, kind=None),
                                                    op=Mult(),
                                                    right=Name(id='total_product_price', ctx=Load()),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice of the project from SO2 should include the milestone to invoice minus the downpayment', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Attribute(
                                                    value=Name(id='expense1', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be the expense amount', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='expense1', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The expense cost of the project from SO1 should be expense amount', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
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
                    name='test_milestone_no_tracking',
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
                            targets=[Name(id='rounding', ctx=Store())],
                            value=Attribute(
                                value=Name(id='currency', ctx=Load()),
                                attr='rounding',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='so_line_deliver_no_task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='price_unit', kind=None),
                                            Constant(value='order_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_manual1',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_manual1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=50, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_manual1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_manual1',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order_2',
                                                    ctx=Load(),
                                                ),
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
                                    value=Name(id='so_line_deliver_no_task', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='qty_delivered', kind=None)],
                                        values=[Constant(value=1.0, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order_2',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='milestone_to_invoice', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_order_project',
                                        ctx=Load(),
                                    ),
                                    attr='price_unit',
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so_line_order_project',
                                        ctx=Load(),
                                    ),
                                    attr='qty_to_invoice',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='milestone_no_task', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='so_line_deliver_no_task', ctx=Load()),
                                    attr='price_unit',
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Attribute(
                                    value=Name(id='so_line_deliver_no_task', ctx=Load()),
                                    attr='qty_to_invoice',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so_line_order_project',
                                    ctx=Load(),
                                ),
                                attr='project_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Name(id='milestone_to_invoice', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='milestone_no_task', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice of the project from SO2 should include the milestone to invoice', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet unit amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_using_milestone_not_tracked', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='sale_line_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Task with milestone not tracked', kind=None),
                                            Attribute(
                                                value=Name(id='project_so_2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='project_so_2', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='so_line_deliver_no_task', ctx=Load()),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Name(id='milestone_to_invoice', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='milestone_no_task', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value="The amount to invoice of the project from SO2 should include the milestone to invoice linked to the project or project's task", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet unit amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The timesheet cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='timesheet', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_log_timesheet_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project_so_2', ctx=Load()),
                                    Constant(value=3, kind=None),
                                    Name(id='task_using_milestone_not_tracked', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_cost', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet', ctx=Load()),
                                attr='amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_timesheet_sold_unit', ctx=Store())],
                            value=Attribute(
                                value=Name(id='timesheet', ctx=Load()),
                                attr='unit_amount',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The invoiced amount of the project from SO2 should only include downpayment not reversed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Name(id='milestone_to_invoice', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='milestone_no_task', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The amount to invoice of the project from SO2 should include the milestone to invoice minus the downpayment', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                    Constant(value='active_id', kind=None),
                                    Constant(value='open_invoices', kind=None),
                                    Constant(value='mail_notrack', kind=None),
                                ],
                                values=[
                                    Constant(value='sale.order', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order_2',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order_2',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
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
                                                slice=Constant(value='sale.advance.payment.inv', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mail_notrack',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='advance_payment_method', kind=None)],
                                        values=[Constant(value='delivered', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action_invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='payment', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create_invoices',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_payment', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='action_invoice', ctx=Load()),
                                        slice=Constant(value='res_id', kind=None),
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
                                    value=Name(id='invoice_payment', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        slice=Constant(value='project.profitability.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project_so_2_stat', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='project.profitability.report', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='read_group',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='project_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='project_so_2', ctx=Load()),
                                                            attr='ids',
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
                                                Constant(value='project_id', kind=None),
                                                Constant(value='amount_untaxed_to_invoice', kind=None),
                                                Constant(value='amount_untaxed_invoiced', kind=None),
                                                Constant(value='timesheet_unit_amount', kind=None),
                                                Constant(value='timesheet_cost', kind=None),
                                                Constant(value='expense_cost', kind=None),
                                                Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                Constant(value='other_revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='project_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Name(id='milestone_to_invoice', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='milestone_no_task', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The invoiced amount of the project from SO2 should include the milestone invoiced', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The amount to invoice of the project from SO2 should include the milestone to invoice', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_sold_unit', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet unit amount of the project from SO2 should include all timesheet in project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='timesheet_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='project_so_2_timesheet_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='The timesheet cost of the project from SO2 should include all timesheet', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost to reinvoice of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense invoiced amount of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='expense_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The expense cost of the project from SO2 should be 0.0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='project_so_2_stat', ctx=Load()),
                                                slice=Constant(value='other_revenues', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='rounding', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='The other revenues of the project from SO2 should be 0.0', kind=None),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
