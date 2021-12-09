Module(
    body=[
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
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
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='AccessError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccountAnalyticLine',
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
                    value=Constant(value='account.analytic.line', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_list', annotation=None, type_comment=None),
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
                                        args=[
                                            Name(id='AccountAnalyticLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='field_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='encoding_uom_id', kind=None),
                                ops=[In()],
                                comparators=[Name(id='field_list', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='encoding_uom_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
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
                                            args=[Constant(value='default_employee_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Compare(
                                        left=Constant(value='employee_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='field_list', ctx=Load())],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='employee_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='hr.employee', kind=None),
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
                                                                Constant(value='user_id', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Subscript(
                                                                    value=Name(id='result', ctx=Load()),
                                                                    slice=Constant(value='user_id', kind=None),
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
                                                    arg='limit',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
                    name='_domain_project_id',
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
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='allow_timesheets', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_has_groups',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='hr_timesheet.group_timesheet_manager', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
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
                                                            Constant(value='|', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='privacy_visibility', kind=None),
                                                                    Constant(value='!=', kind=None),
                                                                    Constant(value='followers', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='message_partner_ids', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Attribute(
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
                                                                                    attr='partner_id',
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
                                                        ctx=Load(),
                                                    ),
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
                        Return(
                            value=Name(id='domain', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_domain_employee_id',
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
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_has_groups',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='hr_timesheet.group_hr_timesheet_approver', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='user_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
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
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_domain_task_id',
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
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_has_groups',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='hr_timesheet.group_hr_timesheet_approver', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='privacy_visibility', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value='followers', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='message_partner_ids', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Attribute(
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
                                                                    attr='partner_id',
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
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
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
                            Constant(value='Task', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_task_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', '=', company_id), ('project_id.allow_timesheets', '=', True), ('project_id', '=?', project_id)]", kind=None),
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
                                arg='compute',
                                value=Constant(value='_compute_project_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Name(id='_domain_project_id', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_user_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='employee_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='hr.employee', kind=None),
                            Constant(value='Employee', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Name(id='_domain_employee_id', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='department_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='hr.department', kind=None),
                            Constant(value='Department', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_department_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
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
                    targets=[Name(id='encoding_uom_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='uom.uom', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_encoding_uom_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_partner_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='name_get',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='name_get',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheets_read', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
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
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
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
                                            Constant(value='id', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='timesheets_read', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='result', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        FunctionDef(
                            name='_get_display_name',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='project_id', annotation=None, type_comment=None),
                                    arg(arg='task_id', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Get the display name of the timesheet based on the project and task\n                :param project_id: tuple containing the id and the display name of the project\n                :param task_id: tuple containing the id and the display name of the task if a task exists in the timesheet\n                              otherwise False.\n                :returns: the display name of the timesheet\n            ', kind=None),
                                ),
                                If(
                                    test=Name(id='task_id', ctx=Load()),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Constant(value='%s - %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='project_id', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='task_id', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='project_id', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet_dict', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='id', kind=None),
                                    ctx=Load(),
                                ),
                                value=Call(
                                    func=Name(id='_get_display_name', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='project_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='task_id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='res', ctx=Store()),
                                        iter=Name(id='timesheets_read', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Dict(
                                                keys=[
                                                    None,
                                                    None,
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[Name(id='result', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Name(id='timesheet_dict', ctx=Load()),
                                                ],
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
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
                    name='_compute_encoding_uom_id',
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
                            target=Name(id='analytic_line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='analytic_line', ctx=Load()),
                                            attr='encoding_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='analytic_line', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='timesheet_encode_uom_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
                    name='_compute_partner_id',
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
                            target=Name(id='timesheet', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='timesheet', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='timesheet', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='timesheet', ctx=Load()),
                                                            attr='task_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='timesheet', ctx=Load()),
                                                            attr='project_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
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
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='task_id.partner_id', kind=None),
                                Constant(value='project_id.partner_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_project_id',
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
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='project_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='project_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
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
                                Constant(value='task_id', kind=None),
                                Constant(value='task_id.project_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_task_id',
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
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='project_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='task_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
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
                            args=[Constant(value='project_id', kind=None)],
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='project_id',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='task_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
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
                    name='_compute_user_id',
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
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='user_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='employee_id',
                                            ctx=Load(),
                                        ),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='employee_id',
                                                ctx=Load(),
                                            ),
                                            attr='user_id',
                                            ctx=Load(),
                                        ),
                                        orelse=Call(
                                            func=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='_default_user',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
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
                            args=[Constant(value='employee_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_department_id',
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
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='department_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='employee_id',
                                            ctx=Load(),
                                        ),
                                        attr='department_id',
                                        ctx=Load(),
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
                            args=[Constant(value='employee_id', kind=None)],
                            keywords=[],
                        ),
                    ],
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
                            targets=[Name(id='default_user_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_default_user',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='map', ctx=Load()),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='x', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Call(
                                                    func=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='user_id', kind=None),
                                                        Name(id='default_user_id', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Name(id='filter', ctx=Load()),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='x', annotation=None, type_comment=None)],
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
                                                                    operand=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='x', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='employee_id', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='x', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='project_id', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Name(id='vals_list', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employees', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.employee', kind=None),
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
                                                    Constant(value='user_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='user_ids', ctx=Load()),
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
                            targets=[Name(id='user_map', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Attribute(
                                        value=Name(id='employee', ctx=Load()),
                                        attr='user_id',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Attribute(
                                    value=Name(id='employee', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='employee', ctx=Store()),
                                        iter=Name(id='employees', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='vals', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='project_id', kind=None)],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='vals', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='name', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='/', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='vals', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='employee_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='project_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='employee_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='user_map', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='vals', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='user_id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Name(id='default_user_id', ctx=Load()),
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
                                            value=Name(id='vals', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_timesheet_preprocess',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='vals', ctx=Load())],
                                                keywords=[],
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
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountAnalyticLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
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
                            target=Tuple(
                                elts=[
                                    Name(id='line', ctx=Store()),
                                    Name(id='values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='lines', ctx=Load()),
                                    Name(id='vals_list', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='_timesheet_postprocess',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=Or(),
                                            values=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_has_groups',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='hr_timesheet.group_hr_timesheet_approver', kind=None)],
                                                    keywords=[],
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='su',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='analytic_line', ctx=Load()),
                                                                attr='user_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='analytic_line', ctx=Store()),
                                                        iter=Name(id='self', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You cannot access timesheets that are not yours.', kind=None)],
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_timesheet_preprocess',
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
                                        left=Constant(value='name', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='name', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
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
                                    value=Constant(value='/', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountAnalyticLine', ctx=Load()),
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
                            type_comment=None,
                        ),
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
                                                    args=[arg(arg='t', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='t', ctx=Load()),
                                                    attr='project_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_timesheet_postprocess',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
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
                    name='fields_view_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='view_id', annotation=None, type_comment=None),
                            arg(arg='view_type', annotation=None, type_comment=None),
                            arg(arg='toolbar', annotation=None, type_comment=None),
                            arg(arg='submenu', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='form', kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Set the correct label for `unit_amount`, depending on company UoM ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountAnalyticLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='fields_view_get',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='view_id',
                                        value=Name(id='view_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='view_type',
                                        value=Name(id='view_type', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='toolbar',
                                        value=Name(id='toolbar', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='submenu',
                                        value=Name(id='submenu', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='arch', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_apply_timesheet_label',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='arch', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='view_type',
                                        value=Name(id='view_type', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
                    name='_apply_timesheet_label',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='view_arch', annotation=None, type_comment=None),
                            arg(arg='view_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='form', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='doc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='XML',
                                    ctx=Load(),
                                ),
                                args=[Name(id='view_arch', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='encoding_uom', ctx=Store())],
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
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='node', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='doc', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="//field[@name='unit_amount'][@widget='timesheet_uom'][not(@string)]", kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='string', kind=None),
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='%s Spent', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='sub',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='[\\(\\)]', kind=None),
                                                        Constant(value='', kind=None),
                                                        BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='encoding_uom', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='', kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='tostring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='doc', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='encoding',
                                        value=Constant(value='unicode', kind=None),
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
                    name='_apply_time_label',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='view_arch', annotation=None, type_comment=None),
                            arg(arg='related_model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='doc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='XML',
                                    ctx=Load(),
                                ),
                                args=[Name(id='view_arch', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Name(id='related_model', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='encoding_uom_name', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
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
                                                    attr='timesheet_encode_uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='prefetch_fields',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='node', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='doc', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="//field[@widget='timesheet_uom'][not(@string)] | //field[@widget='timesheet_uom_no_toggle'][not(@string)]", kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name_with_uom', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Hours', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value='|Hours', kind=None),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='encoding_uom_name', ctx=Load()),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='Model', ctx=Load()),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Call(
                                                            func=Attribute(
                                                                value=Name(id='node', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='name', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_description_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='flags',
                                                value=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='IGNORECASE',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='string', kind=None),
                                            Name(id='name_with_uom', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='tostring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='doc', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='encoding',
                                        value=Constant(value='unicode', kind=None),
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
                    name='_timesheet_get_portal_domain',
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
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='hr_timesheet.group_hr_timesheet_user', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.rule', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_compute_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_name',
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
                            value=List(
                                elts=[
                                    Constant(value='&', kind=None),
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='task_id.project_id.message_partner_ids', kind=None),
                                            Constant(value='child_of', kind=None),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
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
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='commercial_partner_id',
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
                                    Tuple(
                                        elts=[
                                            Constant(value='task_id.message_partner_ids', kind=None),
                                            Constant(value='child_of', kind=None),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
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
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='commercial_partner_id',
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
                                    Tuple(
                                        elts=[
                                            Constant(value='task_id.project_id.privacy_visibility', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='portal', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
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
                    name='_timesheet_preprocess',
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
                        Expr(
                            value=Constant(value=' Deduce other field values from the one given.\n            Overrride this to compute on the fly some field that can not be computed fields.\n            :param values: dict values for `create`or `write`.\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='task_id', kind=None)],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='account_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='task', ctx=Store())],
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
                                                args=[Constant(value='task_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='task_analytic_account_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task', ctx=Load()),
                                            attr='_get_task_analytic_account_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='account_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='task_analytic_account_id', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='company_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task_analytic_account_id', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='tag_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='tag_ids', kind=None),
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
                                                            value=Name(id='task', ctx=Load()),
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
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='tag_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='task', ctx=Load()),
                                                                    attr='analytic_tag_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='task_analytic_account_id', ctx=Load()),
                                            attr='active',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You cannot add timesheets to a project or a task linked to an inactive analytic account.', kind=None)],
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
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='project_id', kind=None)],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='account_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
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
                                                args=[Constant(value='project_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='account_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='analytic_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='company_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='project', ctx=Load()),
                                                        attr='analytic_account_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_id',
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
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='analytic_account_id',
                                                ctx=Load(),
                                            ),
                                            attr='active',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You cannot add timesheets to a project linked to an inactive analytic account.', kind=None)],
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
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='employee_id', kind=None)],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='user_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='employee', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='hr.employee', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='employee_id', kind=None),
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
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='user_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='employee', ctx=Load()),
                                            attr='user_id',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='project_id', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='task_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='partner_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_id', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='task_id', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partner_id', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
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
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vals', ctx=Load()),
                                                                slice=Constant(value='task_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='partner_id',
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
                                            targets=[Name(id='partner_id', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
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
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vals', ctx=Load()),
                                                                slice=Constant(value='project_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=Name(id='partner_id', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='partner_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='partner_id', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='product_uom_id', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='v', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[Name(id='vals', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='v', ctx=Store()),
                                                        iter=List(
                                                            elts=[
                                                                Constant(value='account_id', kind=None),
                                                                Constant(value='project_id', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='analytic_account', ctx=Store())],
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
                                                        slice=Constant(value='account.analytic.account', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='account_id', kind=None),
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
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='product_uom_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='analytic_account', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='project_time_mode_id',
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
                        Return(
                            value=Name(id='vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_timesheet_postprocess',
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
                        Expr(
                            value=Constant(value=' Hook to update record one by one according to the values of a `write` or a `create`. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sudo_self', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values_to_write', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_timesheet_postprocess_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='timesheet', ctx=Store()),
                            iter=Name(id='sudo_self', ctx=Load()),
                            body=[
                                If(
                                    test=Subscript(
                                        value=Name(id='values_to_write', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='timesheet', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='timesheet', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='values_to_write', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='timesheet', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
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
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_timesheet_postprocess_values',
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
                        Expr(
                            value=Constant(value=" Get the addionnal values to write on record\n            :param dict values: values for the model's fields, as a dictionary::\n                {'field_name': field_value, ...}\n            :return: a dictionary mapping each record id to its corresponding\n                dictionary values to write (may be empty).\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=DictComp(
                                key=Name(id='id_', ctx=Load()),
                                value=Dict(keys=[], values=[]),
                                generators=[
                                    comprehension(
                                        target=Name(id='id_', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sudo_self', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Name(id='field_name', ctx=Load()),
                                            ops=[In()],
                                            comparators=[Name(id='values', ctx=Load())],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field_name', ctx=Store()),
                                                iter=List(
                                                    elts=[
                                                        Constant(value='unit_amount', kind=None),
                                                        Constant(value='employee_id', kind=None),
                                                        Constant(value='account_id', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='timesheet', ctx=Store()),
                                    iter=Name(id='sudo_self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='cost', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='timesheet', ctx=Load()),
                                                    attr='_employee_timesheet_cost',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='amount', ctx=Store())],
                                            value=BinOp(
                                                left=UnaryOp(
                                                    op=USub(),
                                                    operand=Attribute(
                                                        value=Name(id='timesheet', ctx=Load()),
                                                        attr='unit_amount',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Mult(),
                                                right=Name(id='cost', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='amount_converted', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='timesheet', ctx=Load()),
                                                            attr='employee_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_convert',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='amount', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='timesheet', ctx=Load()),
                                                            attr='account_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='currency_id',
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
                                                    Attribute(
                                                        value=Name(id='timesheet', ctx=Load()),
                                                        attr='date',
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
                                                    value=Subscript(
                                                        value=Name(id='result', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='timesheet', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='amount', kind=None)],
                                                        values=[Name(id='amount_converted', ctx=Load())],
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
                    name='_is_timesheet_encode_uom_day',
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
                            targets=[Name(id='company_uom', ctx=Store())],
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
                            type_comment=None,
                        ),
                        Return(
                            value=Compare(
                                left=Name(id='company_uom', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='uom.product_uom_day', kind=None)],
                                        keywords=[],
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
                    name='_convert_hours_to_days',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='time', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='uom_hour', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_hour', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_day', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_day', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='round', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='uom_hour', ctx=Load()),
                                            attr='_compute_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='time', ctx=Load()),
                                            Name(id='uom_day', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_failure',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
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
                    name='_get_timesheet_time_day',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_convert_hours_to_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='unit_amount',
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
                    name='_employee_timesheet_cost',
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
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='employee_id',
                                            ctx=Load(),
                                        ),
                                        attr='timesheet_cost',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
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
