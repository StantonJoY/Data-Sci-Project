Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='common',
            names=[alias(name='TestCommonSaleTimesheet', asname=None)],
            level=1,
        ),
        ClassDef(
            name='TestEditSoLineTimesheet',
            bases=[Name(id='TestCommonSaleTimesheet', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='task_rate_task',
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='sale_line_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Task', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_task_rate',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='so',
                                                            ctx=Load(),
                                                        ),
                                                        attr='order_line',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_sol_no_change_if_edited',
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
                            value=Constant(value=' Check if a sol manually edited, does not change with a change of sol in the task.\n\n            Test Case:\n            =========\n            1) create some timesheets on this task,\n            2) edit a SOL of a timesheet in this task,\n            3) check if the edited SOL has the one selected and is not the one in the task,\n            4) change the sol on the task,\n            5) check if the timesheet in which the sol has manually edited, does not change but the another ones are the case.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='timesheet', ctx=Store())],
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
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Line', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_task_rate',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='task_rate_task',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_manager',
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
                                    value=Name(id='timesheet', ctx=Load()),
                                    attr='_compute_so_line',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='edited_timesheet', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='timesheet', ctx=Load()),
                                    attr='copy',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='timesheet', ctx=Load()),
                                            attr='so_line',
                                            ctx=Load(),
                                        ),
                                        ops=[
                                            Eq(),
                                            Eq(),
                                        ],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='edited_timesheet', ctx=Load()),
                                                attr='so_line',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='task_rate_task',
                                                    ctx=Load(),
                                                ),
                                                attr='sale_line_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='SOL in timesheet should be the same than the one in the task.', kind=None),
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
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='timesheet', ctx=Load()),
                                            attr='unit_amount',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='edited_timesheet', ctx=Load()),
                                            attr='unit_amount',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_rate_task',
                                                ctx=Load(),
                                            ),
                                            attr='sale_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='qty_delivered',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The quantity timesheeted should be increased the quantity delivered in the linked SOL.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='edited_timesheet', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='is_so_line_edited', kind=None),
                                            Constant(value='so_line', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='so',
                                                            ctx=Load(),
                                                        ),
                                                        attr='order_line',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=1, kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so',
                                            ctx=Load(),
                                        ),
                                        attr='order_line',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_qty_delivered',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='edited_timesheet', ctx=Load()),
                                        attr='so_line',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='task_rate_task',
                                            ctx=Load(),
                                        ),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='SOL in timesheet should be different than the one in the task.', kind=None),
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
                                    Attribute(
                                        value=Name(id='edited_timesheet', ctx=Load()),
                                        attr='so_line',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='so',
                                                ctx=Load(),
                                            ),
                                            attr='order_line',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='SOL in timesheet is the one selected when we manually edit in the timesheet', kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_rate_task',
                                                ctx=Load(),
                                            ),
                                            attr='sale_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='qty_delivered',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='timesheet', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The quantity delivered should be the quantity defined in the first timesheet of the task since the so_line in the second timesheet has manually been changed.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='task_rate_task',
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='sale_line_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='so',
                                                            ctx=Load(),
                                                        ),
                                                        attr='order_line',
                                                        ctx=Load(),
                                                    ),
                                                    slice=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='timesheet', ctx=Load()),
                                    attr='_compute_so_line',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='edited_timesheet', ctx=Load()),
                                    attr='_compute_so_line',
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so',
                                            ctx=Load(),
                                        ),
                                        attr='order_line',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_qty_delivered',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='timesheet', ctx=Load()),
                                        attr='so_line',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='task_rate_task',
                                            ctx=Load(),
                                        ),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='SOL in timesheet should be the same than the one in the task.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='edited_timesheet', ctx=Load()),
                                        attr='so_line',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='task_rate_task',
                                            ctx=Load(),
                                        ),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='SOL in timesheet which is manually edited should be different than the one in the task.', kind=None),
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
                                    Attribute(
                                        value=Name(id='edited_timesheet', ctx=Load()),
                                        attr='so_line',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='so',
                                                ctx=Load(),
                                            ),
                                            attr='order_line',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='SOL in timesheet should still be the same', kind=None),
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
