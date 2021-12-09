Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='Command', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.safe_eval',
            names=[alias(name='safe_eval', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.sql',
            names=[
                alias(name='column_exists', asname=None),
                alias(name='create_column', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='SaleOrder',
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
                    value=Constant(value='sale.order', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tasks_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='project.task', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_tasks_ids', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Tasks associated to this sale', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tasks_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Tasks', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_tasks_ids', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='project.group_project_user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='visible_project', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Display project', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_visible_project', kind=None),
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
                    targets=[Name(id='project_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='project.project', kind=None),
                            Constant(value='Project', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[
                                        Constant(value='draft', kind=None),
                                        Constant(value='sent', kind=None),
                                    ],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=False, kind=None),
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
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Select a non billable project on which tasks can be created.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='project_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='project.project', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_project_ids', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Projects', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='project.group_project_user', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Projects used in this sales order.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='project_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Number of Projects', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_project_ids', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='project.group_project_user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_tasks_ids',
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
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='tasks_ids',
                                            ctx=Store(),
                                        ),
                                    ],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='display_project_id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value='False', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='|', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='sale_line_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='order', ctx=Load()),
                                                                    attr='order_line',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='sale_order_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='order', ctx=Load()),
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
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='tasks_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='tasks_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                            args=[Constant(value='order_line.product_id.project_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_visible_project',
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
                            value=Constant(value=" Users should be able to select a project_id on the SO if at least one SO line has a product with its service tracking\n        configured as 'task_in_project' ", kind=None),
                        ),
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='visible_project',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='service_tracking', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='task_in_project', kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='service_tracking', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='order', ctx=Load()),
                                                                    attr='order_line',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='product_id.service_tracking', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                            args=[Constant(value='order_line.product_id.service_tracking', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_project_ids',
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
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='projects', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='product_id.project_id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='projects', ctx=Store()),
                                    op=BitOr(),
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='project_id', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='projects', ctx=Store()),
                                    op=BitOr(),
                                    value=Attribute(
                                        value=Name(id='order', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='project_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='projects', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='project_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='projects', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                                Constant(value='order_line.product_id', kind=None),
                                Constant(value='order_line.project_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_project_id',
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
                            value=Constant(value=" Set the SO analytic account to the selected project's analytic account ", kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='project_id',
                                    ctx=Load(),
                                ),
                                attr='analytic_account_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='analytic_account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='analytic_account_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
                            args=[Constant(value='project_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_action_confirm',
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
                            value=Constant(value=' On SO confirmation, some lines should generate a task or a project. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='order_line',
                                                                ctx=Load(),
                                                            ),
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
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_timesheet_service_generation',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                For(
                                    target=Name(id='order', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='order', ctx=Load()),
                                                                        attr='order_line',
                                                                        ctx=Load(),
                                                                    ),
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
                                                                value=Name(id='order', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='_timesheet_service_generation',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_task',
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
                            targets=[Name(id='list_view_id', ctx=Store())],
                            value=Attribute(
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
                                    args=[Constant(value='project.view_task_tree2', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='form_view_id', ctx=Store())],
                            value=Attribute(
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
                                    args=[Constant(value='project.view_task_form2', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='type', kind=None)],
                                values=[Constant(value='ir.actions.act_window_close', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_projects', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tasks_ids',
                                        ctx=Load(),
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='project_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='task_projects', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tasks_ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='action', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='active_id',
                                                                value=Attribute(
                                                                    value=Name(id='task_projects', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.actions.actions', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_for_xml_id',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='project.act_project_project_2_project_task_all', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='domain', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tasks_ids',
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
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='context', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='eval_context', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.actions.actions', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_eval_context',
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
                                                    value=Name(id='eval_context', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='active_id', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='task_projects', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='action_context', ctx=Store())],
                                            value=Call(
                                                func=Name(id='safe_eval', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='action', ctx=Load()),
                                                        slice=Constant(value='context', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='eval_context', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='action_context', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='eval_context', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='context', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='action_context', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='action', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.actions.actions', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_for_xml_id',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='project.action_view_task', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='context', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tasks_ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='views', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='kanban', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Name(id='list_view_id', ctx=Load()),
                                                            Constant(value='tree', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Name(id='form_view_id', ctx=Load()),
                                                            Constant(value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='graph', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='calendar', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='pivot', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tasks_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='action', ctx=Load()),
                                                            slice=Constant(value='views', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='form_view_id', ctx=Load()),
                                                                    Constant(value='form', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='action', ctx=Load()),
                                                            slice=Constant(value='res_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tasks_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='action', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='context', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='action', ctx=Load()),
                                        slice=Constant(value='context', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='search_default_sale_order_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_project_ids',
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
                            targets=[Name(id='view_form_id', ctx=Store())],
                            value=Attribute(
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
                                    args=[Constant(value='project.edit_project', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view_kanban_id', ctx=Store())],
                            value=Attribute(
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
                                    args=[Constant(value='project.view_project_kanban', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='res_model', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='project_ids',
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
                                    Constant(value='kanban,form', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Projects', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='project.project', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='project_ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='views', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='view_form_id', ctx=Load()),
                                                                    Constant(value='form', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='project_ids',
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
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='views', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Name(id='view_kanban_id', ctx=Load()),
                                                    Constant(value='kanban', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='view_form_id', ctx=Load()),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
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
                                        left=Constant(value='state', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='state', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='cancel', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='project_id',
                                                ctx=Load(),
                                            ),
                                            attr='sale_line_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
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
                                            Name(id='SaleOrder', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
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
        ClassDef(
            name='SaleOrderLine',
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
                    value=Constant(value='sale.order.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='project_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='project.project', kind=None),
                            Constant(value='Generated Project', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Project generated by the sales order item', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='task_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='project.task', kind=None),
                            Constant(value='Generated Task', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Task generated by the sales order item', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_service', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is a Service', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_is_service', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sales Order item should generate a task and/or a project, depending on the product settings.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_is_service',
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
                            target=Name(id='so_line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='so_line', ctx=Load()),
                                            attr='is_service',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='so_line', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='service', kind=None)],
                                    ),
                                    type_comment=None,
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
                            args=[Constant(value='product_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_product_updatable',
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
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='service', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='sale', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_updatable',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='super', ctx=Load()),
                                                        args=[
                                                            Name(id='SaleOrderLine', ctx=Load()),
                                                            Name(id='line', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='_compute_product_updatable',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
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
                            args=[Constant(value='product_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_auto_init',
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
                            value=Constant(value='\n        Create column to stop ORM from computing it himself (too slow)\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='column_exists', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='cr',
                                            ctx=Load(),
                                        ),
                                        Constant(value='sale_order_line', kind=None),
                                        Constant(value='is_service', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='create_column', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            Constant(value='sale_order_line', kind=None),
                                            Constant(value='is_service', kind=None),
                                            Constant(value='bool', kind=None),
                                        ],
                                        keywords=[],
                                    ),
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
                                        args=[Constant(value="\n                UPDATE sale_order_line line\n                SET is_service = (pt.type = 'service')\n                FROM product_product pp\n                LEFT JOIN product_template pt ON pt.id = pp.product_tmpl_id\n                WHERE pp.id = line.product_id\n            ", kind=None)],
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_auto_init',
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
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='lines', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='sale', kind=None)],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='is_expense',
                                                    ctx=Load(),
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
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='_timesheet_service_generation',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='task_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='msg_body', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Task Created (%s): <a href=# data-oe-model=project.task data-oe-id=%d>%s</a>', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='task_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='task_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='message_post',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='body',
                                                                value=Name(id='msg_body', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
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
                        Return(
                            value=Name(id='lines', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
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
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='product_uom_qty', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
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
                                            args=[
                                                Constant(value='no_update_planned_hours', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='task_id',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='service', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='planned_hours', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='_convert_qty_company_hours',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='task_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='company_id',
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
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='task_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='planned_hours', kind=None)],
                                                                values=[Name(id='planned_hours', ctx=Load())],
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_convert_qty_company_hours',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='dest_company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_uom_qty',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_timesheet_create_project_prepare_values',
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
                            value=Constant(value='Generate project values', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='account', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='order_id',
                                    ctx=Load(),
                                ),
                                attr='analytic_account_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='account', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='_create_analytic_account',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='prefix',
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='default_code',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=None, kind=None),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='account', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='analytic_account_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='analytic_account_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='sale_line_id', kind=None),
                                    Constant(value='active', kind=None),
                                    Constant(value='company_id', kind=None),
                                ],
                                values=[
                                    IfExp(
                                        test=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='client_order_ref',
                                            ctx=Load(),
                                        ),
                                        body=BinOp(
                                            left=Constant(value='%s - %s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='client_order_ref',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        orelse=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='account', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
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
                    name='_timesheet_create_project',
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
                            value=Constant(value=' Generate project for the given so line, and link it.\n            :param project: record of project.project in which the task should be created\n            :return task: record of the created task\n        ', kind=None),
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_timesheet_create_project_prepare_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product_id',
                                    ctx=Load(),
                                ),
                                attr='project_template_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s - %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='project_template_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='project', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='project_template_id',
                                                ctx=Load(),
                                            ),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='tasks',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='sale_line_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='email',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='project', ctx=Load()),
                                                        attr='tasks',
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='task', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='task', ctx=Load()),
                                                                attr='parent_id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotEq()],
                                                            comparators=[Constant(value=False, kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='sale_line_id', kind=None),
                                                    Constant(value='sale_order_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='project', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='project.project', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='project', ctx=Load()),
                                    attr='type_ids',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='type_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='project.task.type', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='New', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='project_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='project', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_timesheet_create_task_prepare_values',
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
                            targets=[Name(id='planned_hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_convert_qty_company_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sale_line_name_parts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='title', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='sale_line_name_parts', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='description', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='<br/>', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='sale_line_name_parts', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='planned_hours', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='email_from', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='project_id', kind=None),
                                    Constant(value='sale_line_id', kind=None),
                                    Constant(value='sale_order_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='user_ids', kind=None),
                                ],
                                values=[
                                    IfExp(
                                        test=Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='sale_line_id',
                                            ctx=Load(),
                                        ),
                                        body=Name(id='title', ctx=Load()),
                                        orelse=BinOp(
                                            left=Constant(value='%s: %s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='order_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='title', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    Name(id='planned_hours', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    Name(id='description', ctx=Load()),
                                    Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_timesheet_create_task',
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
                        Expr(
                            value=Constant(value=' Generate task for the given so line, and link it.\n            :param project: record of project.project in which the task should be created\n            :return task: record of the created task\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_timesheet_create_task_prepare_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='project', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
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
                                                slice=Constant(value='project.task', kind=None),
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
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='task_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_msg', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='This task has been created from: <a href=# data-oe-model=sale.order data-oe-id=%d>%s</a> (%s)', kind=None)],
                                    keywords=[],
                                ),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task', ctx=Load()),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=Name(id='task_msg', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='task', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_timesheet_service_generation',
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
                            value=Constant(value=" For service lines, create the task or the project. If already exists, it simply links\n            the existing one to the line.\n            Note: If the SO was confirmed, cancelled, set to draft then confirmed, avoid creating a\n            new project/task. This explains the searches on 'sale_line_id' on project/task. This also\n            implied if so line of generated task has been modified, we may regenerate it.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='so_line_task_global_project', ctx=Store())],
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
                                            args=[arg(arg='sol', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='sol', ctx=Load()),
                                                    attr='is_service',
                                                    ctx=Load(),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='sol', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='service_tracking',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='task_global_project', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='so_line_new_project', ctx=Store())],
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
                                            args=[arg(arg='sol', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='sol', ctx=Load()),
                                                    attr='is_service',
                                                    ctx=Load(),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='sol', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='service_tracking',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='project_only', kind=None),
                                                                Constant(value='task_in_project', kind=None),
                                                            ],
                                                            ctx=Load(),
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
                        Assign(
                            targets=[Name(id='map_so_project', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='so_line_new_project', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='order_ids', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='order_id', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='so_lines_with_project', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='order_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='order_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='project_id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='product_id.service_tracking', kind=None),
                                                            Constant(value='in', kind=None),
                                                            List(
                                                                elts=[
                                                                    Constant(value='project_only', kind=None),
                                                                    Constant(value='task_in_project', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='product_id.project_template_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
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
                                    targets=[Name(id='map_so_project', ctx=Store())],
                                    value=DictComp(
                                        key=Attribute(
                                            value=Attribute(
                                                value=Name(id='sol', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        value=Attribute(
                                            value=Name(id='sol', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='sol', ctx=Store()),
                                                iter=Name(id='so_lines_with_project', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='so_lines_with_project_templates', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='order_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='order_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='project_id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='product_id.service_tracking', kind=None),
                                                            Constant(value='in', kind=None),
                                                            List(
                                                                elts=[
                                                                    Constant(value='project_only', kind=None),
                                                                    Constant(value='task_in_project', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='product_id.project_template_id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
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
                                    targets=[Name(id='map_so_project_templates', ctx=Store())],
                                    value=DictComp(
                                        key=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sol', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='sol', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='project_template_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        value=Attribute(
                                            value=Name(id='sol', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='sol', ctx=Store()),
                                                iter=Name(id='so_lines_with_project_templates', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='map_sol_project', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='so_line_task_global_project', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='map_sol_project', ctx=Store())],
                                    value=DictComp(
                                        key=Attribute(
                                            value=Name(id='sol', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sol', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_company',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='sol', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='sol', ctx=Store()),
                                                iter=Name(id='so_line_task_global_project', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        FunctionDef(
                            name='_can_create_project',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='sol', annotation=None, type_comment=None)],
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
                                            value=Name(id='sol', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        If(
                                            test=Attribute(
                                                value=Attribute(
                                                    value=Name(id='sol', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='project_template_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Return(
                                                    value=Compare(
                                                        left=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='sol', ctx=Load()),
                                                                        attr='order_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='sol', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='project_template_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='map_so_project_templates', ctx=Load())],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='sol', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='map_so_project', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Constant(value=True, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_determine_project',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='so_line', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value="Determine the project for this sale order line.\n            Rules are different based on the service_tracking:\n\n            - 'project_only': the project_id can only come from the sale order line itself\n            - 'task_in_project': the project_id comes from the sale order line only if no project_id was configured\n              on the parent sale order", kind=None),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='so_line', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='service_tracking',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='project_only', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Name(id='so_line', ctx=Load()),
                                                attr='project_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='so_line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='service_tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='task_in_project', kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='so_line', ctx=Load()),
                                                                    attr='order_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='project_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='so_line', ctx=Load()),
                                                                attr='project_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='so_line', ctx=Store()),
                            iter=Name(id='so_line_task_global_project', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='so_line', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='map_sol_project', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='so_line', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='so_line', ctx=Load()),
                                                            attr='product_uom_qty',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='so_line', ctx=Load()),
                                                            attr='_timesheet_create_task',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='project',
                                                                value=Subscript(
                                                                    value=Name(id='map_sol_project', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='so_line', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
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
                        For(
                            target=Name(id='so_line', ctx=Store()),
                            iter=Name(id='so_line_new_project', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='project', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_determine_project', ctx=Load()),
                                        args=[Name(id='so_line', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='project', ctx=Load()),
                                            ),
                                            Call(
                                                func=Name(id='_can_create_project', ctx=Load()),
                                                args=[Name(id='so_line', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='project', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='so_line', ctx=Load()),
                                                    attr='_timesheet_create_project',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Attribute(
                                                    value=Name(id='so_line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='project_template_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='map_so_project_templates', ctx=Load()),
                                                            slice=Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='so_line', ctx=Load()),
                                                                            attr='order_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='so_line', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='project_template_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='project', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='map_so_project', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='so_line', ctx=Load()),
                                                                    attr='order_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='project', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='project', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='so_line', ctx=Load()),
                                                            attr='project_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='map_so_project_templates', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='so_line', ctx=Load()),
                                                                                    attr='order_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='so_line', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='project_template_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='map_so_project', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='so_line', ctx=Load()),
                                                                            attr='order_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='so_line', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='service_tracking',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='task_in_project', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='project', ctx=Load()),
                                            ),
                                            body=[
                                                If(
                                                    test=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='so_line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='project_template_id',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='project', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='map_so_project_templates', ctx=Load()),
                                                                slice=Tuple(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='so_line', ctx=Load()),
                                                                                attr='order_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='so_line', ctx=Load()),
                                                                                    attr='product_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='project_template_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='project', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='map_so_project', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='so_line', ctx=Load()),
                                                                        attr='order_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='so_line', ctx=Load()),
                                                    attr='task_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='so_line', ctx=Load()),
                                                            attr='_timesheet_create_task',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='project',
                                                                value=Name(id='project', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_invoice_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='optional_values', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n            If the sale order line isn't linked to a sale order which already have a default analytic account,\n            this method allows to retrieve the analytic account which is linked to project or task directly linked\n            to this sale order line, or the analytic account of the project which uses this sale order line, if it exists.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SaleOrderLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_invoice_line',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='optional_values', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='analytic_account_id', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='analytic_account_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='analytic_account_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='task_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get_task_analytic_account_id',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_id',
                                                    ctx=Load(),
                                                ),
                                                attr='analytic_account_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='analytic_account_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='project_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='analytic_account_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='is_service',
                                                                ctx=Load(),
                                                            ),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='is_expense',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='task_analytic_account_id', ctx=Store())],
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
                                                                    attr='read_group',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='sale_line_id', kind=None),
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
                                                                                    Constant(value='analytic_account_id', kind=None),
                                                                                    Constant(value='!=', kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[Constant(value='analytic_account_id', kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[Constant(value='analytic_account_id', kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='project_analytic_account_id', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='project.project', kind=None),
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
                                                                                    Constant(value='analytic_account_id', kind=None),
                                                                                    Constant(value='!=', kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='|', kind=None),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='sale_line_id', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='&', kind=None),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='tasks.sale_line_id', kind=None),
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
                                                                                    Constant(value='tasks.analytic_account_id', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[Constant(value='analytic_account_id', kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[Constant(value='analytic_account_id', kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='analytic_account_ids', ctx=Store())],
                                                            value=SetComp(
                                                                elt=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='rec', ctx=Load()),
                                                                        slice=Constant(value='analytic_account_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='rec', ctx=Store()),
                                                                        iter=BinOp(
                                                                            left=Name(id='task_analytic_account_id', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Name(id='project_analytic_account_id', ctx=Load()),
                                                                        ),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='analytic_account_ids', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            slice=Constant(value='analytic_account_id', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='analytic_account_ids', ctx=Load()),
                                                                            attr='pop',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
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
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='task_id',
                                    ctx=Load(),
                                ),
                                attr='analytic_tag_ids',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='analytic_tag_ids', kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='Command', ctx=Load()),
                                                attr='link',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='tag_id', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='tag_id', ctx=Store()),
                                                iter=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='analytic_tag_ids',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='is_service',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='is_expense',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='tag_ids', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.analytic.tag', kind=None),
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
                                                                    Constant(value='task_ids.sale_line_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
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
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='analytic_tag_ids', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='Command', ctx=Load()),
                                                        attr='link',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='tag_id', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='tag_id', ctx=Store()),
                                                        iter=Name(id='tag_ids', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
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
