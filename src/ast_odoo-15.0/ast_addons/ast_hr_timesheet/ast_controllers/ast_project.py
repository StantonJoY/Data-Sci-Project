Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.project.controllers.portal',
            names=[alias(name='CustomerPortal', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ProjectCustomerPortal',
            bases=[Name(id='CustomerPortal', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_prepare_project_sharing_session_info',
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
                            targets=[Name(id='session_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_prepare_project_sharing_session_info',
                                    ctx=Load(),
                                ),
                                args=[Name(id='project', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Attribute(
                                value=Name(id='project', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet_encode_uom', ctx=Store())],
                            value=Attribute(
                                value=Name(id='company', ctx=Load()),
                                attr='timesheet_encode_uom_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_time_mode_uom', ctx=Store())],
                            value=Attribute(
                                value=Name(id='company', ctx=Load()),
                                attr='project_time_mode_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='session_info', ctx=Load()),
                                                slice=Constant(value='user_companies', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='allowed_companies', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='timesheet_uom_id',
                                        value=Attribute(
                                            value=Name(id='timesheet_encode_uom', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='timesheet_uom_factor',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='project_time_mode_uom', ctx=Load()),
                                                attr='_compute_quantity',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value=1.0, kind=None),
                                                Name(id='timesheet_encode_uom', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='round',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='session_info', ctx=Load()),
                                    slice=Constant(value='uom_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='uom', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Dict(
                                    keys=[
                                        Constant(value='id', kind=None),
                                        Constant(value='name', kind=None),
                                        Constant(value='rounding', kind=None),
                                        Constant(value='timesheet_widget', kind=None),
                                    ],
                                    values=[
                                        Attribute(
                                            value=Name(id='uom', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='uom', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='uom', ctx=Load()),
                                            attr='rounding',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='uom', ctx=Load()),
                                            attr='timesheet_widget',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='uom', ctx=Store()),
                                        iter=List(
                                            elts=[
                                                Name(id='timesheet_encode_uom', ctx=Load()),
                                                Name(id='project_time_mode_uom', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='session_info', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_task_get_page_view_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='task', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProjectCustomerPortal', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_task_get_page_view_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='task', ctx=Load()),
                                    Name(id='access_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_timesheet_get_portal_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='domain', ctx=Load()),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='task_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='task', ctx=Load()),
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subtask_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='domain', ctx=Load()),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='task_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='task', ctx=Load()),
                                                                    attr='child_ids',
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
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheets', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.analytic.line', kind=None),
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
                                args=[Name(id='task_domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subtasks_timesheets', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.analytic.line', kind=None),
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
                                args=[Name(id='subtask_domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheets_by_subtask', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='account.analytic.line', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='timesheet', ctx=Store()),
                            iter=Name(id='subtasks_timesheets', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='timesheets_by_subtask', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='timesheet', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Name(id='timesheet', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='timesheets', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='timesheets', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='timesheets_by_subtask', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='timesheets_by_subtask', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='is_uom_day', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_is_timesheet_encode_uom_day',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
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
