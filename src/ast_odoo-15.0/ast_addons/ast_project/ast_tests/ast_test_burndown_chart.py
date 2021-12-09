Module(
    body=[
        ImportFrom(
            module='freezegun',
            names=[alias(name='freeze_time', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='Command', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestBurndownChart',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='set_create_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='table', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='create_date', annotation=None, type_comment=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='UPDATE {} SET create_date=%s WHERE id=%s', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='table', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Tuple(
                                        elts=[
                                            Name(id='create_date', ctx=Load()),
                                            Name(id='res_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
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
                    name='test_burndown_chart',
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
                            targets=[Name(id='current_year', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='now',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='year',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='create_date', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='current_year', ctx=Load()),
                                        op=Sub(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='kanban_state_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='legend_blocked', kind=None),
                                    Constant(value='legend_done', kind=None),
                                    Constant(value='legend_normal', kind=None),
                                ],
                                values=[
                                    Constant(value='Blocked', kind=None),
                                    Constant(value='Ready', kind=None),
                                    Constant(value='In Progress', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Stage', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='project.task.type', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='todo_stage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Stage', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='sequence', kind=None),
                                            Constant(value='name', kind=None),
                                            None,
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Constant(value='TODO', kind=None),
                                            Name(id='kanban_state_vals', ctx=Load()),
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task_type', kind=None),
                                    Attribute(
                                        value=Name(id='todo_stage', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='in_progress_stage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Stage', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='sequence', kind=None),
                                            Constant(value='name', kind=None),
                                            None,
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value='In Progress', kind=None),
                                            Name(id='kanban_state_vals', ctx=Load()),
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task_type', kind=None),
                                    Attribute(
                                        value=Name(id='in_progress_stage', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='testing_stage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Stage', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='sequence', kind=None),
                                            Constant(value='name', kind=None),
                                            None,
                                        ],
                                        values=[
                                            Constant(value=20, kind=None),
                                            Constant(value='Testing', kind=None),
                                            Name(id='kanban_state_vals', ctx=Load()),
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task_type', kind=None),
                                    Attribute(
                                        value=Name(id='testing_stage', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='done_stage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Stage', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='sequence', kind=None),
                                            Constant(value='name', kind=None),
                                            None,
                                        ],
                                        values=[
                                            Constant(value=30, kind=None),
                                            Constant(value='Done', kind=None),
                                            Name(id='kanban_state_vals', ctx=Load()),
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task_type', kind=None),
                                    Attribute(
                                        value=Name(id='done_stage', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='stages', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=Name(id='todo_stage', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='in_progress_stage', ctx=Load()),
                                    ),
                                    op=Add(),
                                    right=Name(id='testing_stage', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='done_stage', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='privacy_visibility', kind=None),
                                            Constant(value='alias_name', kind=None),
                                            Constant(value='type_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Burndown Chart Test', kind=None),
                                            Constant(value='employees', kind=None),
                                            Constant(value='project+burndown_chart', kind=None),
                                            ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='Command', ctx=Load()),
                                                        attr='link',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='stage_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='stage_id', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='stages', ctx=Load()),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_project', kind=None),
                                    Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='project', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_a', ctx=Store())],
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
                                            Constant(value='priority', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='stage_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Task A', kind=None),
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='todo_stage', ctx=Load()),
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task', kind=None),
                                    Attribute(
                                        value=Name(id='task_a', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_a', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Task B', kind=None)],
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task', kind=None),
                                    Attribute(
                                        value=Name(id='task_b', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_c', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_a', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Task C', kind=None)],
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task', kind=None),
                                    Attribute(
                                        value=Name(id='task_c', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_d', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_a', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Task D', kind=None)],
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task', kind=None),
                                    Attribute(
                                        value=Name(id='task_d', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_e', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_a', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Task E', kind=None)],
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task', kind=None),
                                    Attribute(
                                        value=Name(id='task_e', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='create_date', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_f', ctx=Store())],
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
                                            Constant(value='priority', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='stage_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Task F', kind=None),
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='todo_stage', ctx=Load()),
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
                                    attr='set_create_date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='project_task', kind=None),
                                    Attribute(
                                        value=Name(id='task_f', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='current_year', ctx=Load()),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            Constant(value=12, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                        keywords=[],
                                    ),
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
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-02-10', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='task_a', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='task_b', ctx=Load()),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='in_progress_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-02-20', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_c', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='in_progress_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-03-15', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='task_d', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='task_e', ctx=Load()),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='in_progress_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-04-10', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='task_a', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='task_b', ctx=Load()),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='testing_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-05-12', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_c', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='testing_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-06-25', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_d', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='testing_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-07-25', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_e', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='testing_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-08-01', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_a', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='done_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-09-10', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_b', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='done_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-10-05', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_c', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='done_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-11-25', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_d', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='done_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s-12-12', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_e', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='stage_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='done_stage', ctx=Load()),
                                                        attr='id',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='read_group_result', ctx=Store())],
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
                                                slice=Constant(value='project.task.burndown.chart.report', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='fill_temporal',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
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
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='project', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='display_project_id', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='date', kind=None),
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='nb_tasks', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='date:month', kind=None),
                                            Constant(value='stage_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='lazy',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='read_group_result_dict', ctx=Store())],
                            value=DictComp(
                                key=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='date:month', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='stage_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='nb_tasks', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='res', ctx=Store()),
                                        iter=Name(id='read_group_result', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stages_dict', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='stage', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Attribute(
                                    value=Name(id='stage', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='stage', ctx=Store()),
                                        iter=Name(id='stages', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_dict', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='January %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='todo_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='February %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='todo_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='February %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='in_progress_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='March %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='in_progress_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='April %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='in_progress_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='April %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='testing_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='May %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='in_progress_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='May %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='testing_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='June %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='in_progress_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='June %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='testing_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='July %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='testing_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='August %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='testing_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='August %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='done_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='September %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='testing_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='September %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='done_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='October %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='testing_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='October %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='done_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='November %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='testing_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='November %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='done_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='December %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='done_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='December %s', kind=None),
                                                op=Mod(),
                                                right=BinOp(
                                                    left=Name(id='current_year', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='todo_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='January %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='current_year', ctx=Load()),
                                            ),
                                            Attribute(
                                                value=Name(id='done_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='January %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='current_year', ctx=Load()),
                                            ),
                                            Attribute(
                                                value=Name(id='todo_stage', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                values=[
                                    Constant(value=5, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Name(id='month', ctx=Store()),
                                            Name(id='stage_id', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    Name(id='nb_tasks', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='read_group_result_dict', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='expected_nb_tasks', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expected_dict', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Name(id='month', ctx=Load()),
                                                    Name(id='stage_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            IfExp(
                                                test=Compare(
                                                    left=Name(id='stage_id', ctx=Load()),
                                                    ops=[NotEq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='todo_stage', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                body=Constant(value=5, kind=None),
                                                orelse=Constant(value=1, kind=None),
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
                                            Name(id='nb_tasks', ctx=Load()),
                                            Name(id='expected_nb_tasks', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='In %s, the number of tasks should be equal to %s in %s stage.', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='month', ctx=Load()),
                                                        Name(id='expected_nb_tasks', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='stages_dict', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='stage_id', ctx=Load()),
                                                                Constant(value='Unknown', kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
