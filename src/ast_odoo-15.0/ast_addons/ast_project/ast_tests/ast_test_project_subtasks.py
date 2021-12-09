Module(
    body=[
        ImportFrom(
            module='odoo.addons.project.tests.test_project_base',
            names=[alias(name='TestProjectCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestProjectSubtasks',
            bases=[Name(id='TestProjectCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_task_display_project_with_default_form',
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
                            value=Constant(value='\n            Create a task in the default task form should take the project set in the form or the default project in the context\n        ', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Test Task 1', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='project_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_form', ctx=Load()),
                                    attr='save',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The project should be assigned.', kind=None),
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The display project of a first layer task should be assigned to project_id.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='tracking_disable', kind=None),
                                                            Constant(value='default_project_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=True, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='project_pigs',
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
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Test Task 2', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_form', ctx=Load()),
                                    attr='save',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The project should be assigned from the default project.', kind=None),
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The display project of a first layer task should be assigned to project_id.', kind=None),
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
                    name='test_task_display_project_with_task_form2',
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
                            value=Constant(value='\n            Create a task in the task form 2 should take the project set in the form or the default project in the context\n        ', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='view',
                                                value=Constant(value='project.view_task_form2', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Test Task 1', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='project_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_form', ctx=Load()),
                                    attr='save',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The project should be assigned.', kind=None),
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The display project of a first layer task should be assigned to project_id.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='tracking_disable', kind=None),
                                                            Constant(value='default_project_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=True, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='project_pigs',
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
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='view',
                                                value=Constant(value='project.view_task_form2', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Test Task 2', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_form', ctx=Load()),
                                    attr='save',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The project should be assigned from the default project.', kind=None),
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The display project of a first layer task should be assigned to project_id.', kind=None),
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
                    name='test_task_display_project_with_quick_create_task_form',
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
                            value=Constant(value='\n            Create a task in the quick create form should take the default project in the context\n        ', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='tracking_disable', kind=None),
                                                            Constant(value='default_project_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=True, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='project_pigs',
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
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='view',
                                                value=Constant(value='project.quick_create_task_form', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Test Task 2', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_form', ctx=Load()),
                                    attr='save',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The project should be assigned from the default project.', kind=None),
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The display project of a first layer task should be assigned to project_id.', kind=None),
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
                    name='test_task_display_project_with_any_task_form',
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
                            value=Constant(value='\n            Create a task in any form should take the default project in the context\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='form_views', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
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
                                                    Constant(value='model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='project.task', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='form', kind=None),
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
                        For(
                            target=Name(id='form_view', ctx=Store()),
                            iter=Name(id='form_views', ctx=Load()),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='Form', ctx=Load()),
                                                args=[
                                                    Call(
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
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tracking_disable', kind=None),
                                                                    Constant(value='default_project_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=True, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='project_pigs',
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
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='view',
                                                        value=Name(id='form_view', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=Name(id='task_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='task_form', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Test Task 1', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='task', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='save',
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='project_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='project_pigs',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='The project should be assigned from the default project, form_view name : %s.', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='form_view', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ),
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
                                                value=Name(id='task', ctx=Load()),
                                                attr='display_project_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='project_id',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='The display project of a first layer task should be assigned to project_id, form_view name : %s.', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='form_view', ctx=Load()),
                                                    attr='name',
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
                FunctionDef(
                    name='test_subtask_display_project',
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
                            value=Constant(value="\n            1) Create a subtask\n                - Should have the same project as its parent\n                - Shouldn't have a display project set.\n            2) Set display project on subtask\n                - Should not change parent project\n                - Should change the subtask project\n                - Display project should be correct\n            3) Reset the display project to False\n                - Should make the project equal to parent project\n                - Display project should be correct\n            4) Change parent task project\n                - Should make the subtask project follow parent project\n                - Display project should stay false\n            5) Set display project on subtask and change parent task project\n                - Should make the subtask project follow new display project id\n                - Display project should be correct\n            6) Remove parent task:\n                - The project id should remain unchanged\n                - The display project id should follow the project id\n            7) Remove display project id then parent id:\n                - The project id should be the one from the parent :\n                    - Since the display project id was removed, the project id is updated to the parent one\n                - The display project id should follow the project id\n        ", kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task_form', ctx=Load()),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='subtask_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='subtask_form', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Test Subtask 1', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The project should be assigned from the default project.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The display project of a sub task should be false to project_id.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task_form', ctx=Load()),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='edit',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='subtask_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='subtask_form', ctx=Load()),
                                                    attr='display_project_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='project_goats',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='task_1',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Changing the project of a subtask should not change parent project', kind=None),
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
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_goats',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Display Project of the task should be well assigned', kind=None),
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
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_goats',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Changing display project id on a subtask should change project id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task_form', ctx=Load()),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='edit',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='subtask_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='subtask_form', ctx=Load()),
                                                    attr='display_project_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='project.project', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Display Project of the task should be well assigned, to False', kind=None),
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
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Resetting display project to False on a subtask should change project id to parent project id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='project_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_goats',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='task_1',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_goats',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Parent project should change.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Display Project of the task should be False', kind=None),
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
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_goats',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Resetting display project to False on a subtask should follow project of its parent', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task_form', ctx=Load()),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='edit',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='subtask_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='subtask_form', ctx=Load()),
                                                    attr='display_project_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='project_goats',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='project_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='task_1',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Parent project should change back.', kind=None),
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
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_goats',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Display Project of the task should be well assigned', kind=None),
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
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_goats',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Changing display project id on a subtask should change project id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='task_1',
                                                            ctx=Load(),
                                                        ),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='subtask_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='subtask_form', ctx=Load()),
                                            attr='parent_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='orphan_subtask', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subtask_form', ctx=Load()),
                                    attr='save',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='orphan_subtask', ctx=Load()),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_goats',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Display Project of the task should be well assigned', kind=None),
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
                                        value=Name(id='orphan_subtask', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_goats',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Changing display project id on a subtask should change project id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='orphan_subtask', ctx=Load()),
                                        attr='parent_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Parent should be false', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task_form', ctx=Load()),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='subtask_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='subtask_form', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Test Subtask 1', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='subtask_form', ctx=Load()),
                                                    attr='display_project_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='project_goats',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='task_1',
                                                            ctx=Load(),
                                                        ),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='subtask_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='subtask_form', ctx=Load()),
                                            attr='display_project_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.project', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='subtask_form', ctx=Load()),
                                            attr='parent_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='orphan_subtask', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subtask_form', ctx=Load()),
                                    attr='save',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='orphan_subtask', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Removing parent should not change project', kind=None),
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
                                        value=Name(id='orphan_subtask', ctx=Load()),
                                        attr='display_project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Removing parent should make the display project set as project.', kind=None),
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
                    name='test_subtask_stage',
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
                            value=Constant(value='\n            The stage of the new child must be the default one of the project\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='stage_a', ctx=Store())],
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
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='a', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stage_b', ctx=Store())],
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
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='b', kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='project_pigs',
                                    ctx=Load(),
                                ),
                                attr='type_ids',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Name(id='stage_a', ctx=Load()),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='project_pigs',
                                    ctx=Load(),
                                ),
                                attr='type_ids',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Name(id='stage_b', ctx=Load()),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task_form', ctx=Load()),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='subtask_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='subtask_form', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Test Subtask 1', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='stage_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='stage_a', ctx=Load()),
                                    Constant(value='The stage of the child task should be the default one of the project.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task_form', ctx=Load()),
                                            attr='stage_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='stage_b', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='stage_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='stage_a', ctx=Load()),
                                    Constant(value='The stage of the child task should remain the same while changing parent task stage.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='task_form', ctx=Load()),
                                                attr='child_ids',
                                                ctx=Load(),
                                            ),
                                            attr='remove',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task_form', ctx=Load()),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='subtask_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='subtask_form', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Test Subtask 2', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='task_1',
                                                ctx=Load(),
                                            ),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                        attr='stage_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='stage_a', ctx=Load()),
                                    Constant(value='The stage of the child task should be the default one of the project even if parent stage id is different.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='tracking_disable', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='task_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task_form', ctx=Load()),
                                                        attr='child_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='edit',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='subtask_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='subtask_form', ctx=Load()),
                                                    attr='display_project_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='project_goats',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='task_1',
                                                    ctx=Load(),
                                                ),
                                                attr='child_ids',
                                                ctx=Load(),
                                            ),
                                            attr='stage_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='New', kind=None),
                                    Constant(value='The stage of the child task should be the default one of the display project id, once set.', kind=None),
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
