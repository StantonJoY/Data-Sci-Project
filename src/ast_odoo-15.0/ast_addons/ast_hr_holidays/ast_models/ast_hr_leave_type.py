Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[alias(name='float_round', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='HolidaysType',
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
                    value=Constant(value='hr.leave.type', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Time Off Type', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_model_sorting_key',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='leave_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='remaining', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='leave_type', ctx=Load()),
                                    attr='virtual_remaining_leaves',
                                    ctx=Load(),
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='taken', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='leave_type', ctx=Load()),
                                    attr='leaves_taken',
                                    ctx=Load(),
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    BinOp(
                                        left=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        op=Mult(),
                                        right=Attribute(
                                            value=Name(id='leave_type', ctx=Load()),
                                            attr='sequence',
                                            ctx=Load(),
                                        ),
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='leave_type', ctx=Load()),
                                                    attr='employee_requests',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='no', kind=None)],
                                            ),
                                            Name(id='remaining', ctx=Load()),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='leave_type', ctx=Load()),
                                                    attr='employee_requests',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='yes', kind=None)],
                                            ),
                                            Name(id='remaining', ctx=Load()),
                                        ],
                                    ),
                                    Name(id='taken', ctx=Load()),
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
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Time Off Type', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=100, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The type with the smallest sequence is the default value in time off request', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='create_calendar_meeting', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Display Time Off in Calendar', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='color_name', ctx=Store())],
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
                                            Constant(value='red', kind=None),
                                            Constant(value='Red', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='blue', kind=None),
                                            Constant(value='Blue', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lightgreen', kind=None),
                                            Constant(value='Light Green', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lightblue', kind=None),
                                            Constant(value='Light Blue', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lightyellow', kind=None),
                                            Constant(value='Light Yellow', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='magenta', kind=None),
                                            Constant(value='Magenta', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lightcyan', kind=None),
                                            Constant(value='Light Cyan', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='black', kind=None),
                                            Constant(value='Black', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lightpink', kind=None),
                                            Constant(value='Light Pink', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='brown', kind=None),
                                            Constant(value='Brown', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='violet', kind=None),
                                            Constant(value='Violet', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lightcoral', kind=None),
                                            Constant(value='Light Coral', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lightsalmon', kind=None),
                                            Constant(value='Light Salmon', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lavender', kind=None),
                                            Constant(value='Lavender', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='wheat', kind=None),
                                            Constant(value='Wheat', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='ivory', kind=None),
                                            Constant(value='Ivory', kind=None),
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
                                value=Constant(value='Color in Report', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='red', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This color will be used in the time off summary located in Reporting > Time off by Department.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='color', ctx=Store())],
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
                                value=Constant(value='Color', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The color selected here will be used in every screen with the time off type.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='icon_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.attachment', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Cover Image', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('res_model', '=', 'hr.leave.type'), ('res_field', '=', 'icon_id')]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Active', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If the active field is set to false, it will allow you to hide the time off type without removing it.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='max_leaves', ctx=Store())],
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
                                value=Constant(value='_compute_leaves', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Maximum Allowed', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_max_leaves', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This value is given by the sum of all time off requests with a positive value.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='leaves_taken', ctx=Store())],
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
                                value=Constant(value='_compute_leaves', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Time off Already Taken', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This value is given by the sum of all time off requests with a negative value.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='remaining_leaves', ctx=Store())],
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
                                value=Constant(value='_compute_leaves', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Remaining Time Off', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Maximum Time Off Allowed - Time Off Already Taken', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='virtual_remaining_leaves', ctx=Store())],
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
                                value=Constant(value='_compute_leaves', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_virtual_remaining_leaves', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Virtual Remaining Time Off', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Maximum Time Off Allowed - Time Off Already Taken - Time Off Waiting Approval', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='virtual_leaves_taken', ctx=Store())],
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
                                value=Constant(value='_compute_leaves', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Virtual Time Off Already Taken', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sum of validated and non validated time off requests.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_days_allocation', ctx=Store())],
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
                                value=Constant(value='_compute_group_days_allocation', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Days Allocated', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_days_leave', ctx=Store())],
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
                                value=Constant(value='_compute_group_days_leave', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Group Time Off', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='responsible_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users', kind=None),
                            Constant(value='Responsible Time Off Officer', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='groups_id', kind=None),
                                                    Constant(value='in', kind=None),
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
                                                            args=[Constant(value='hr_holidays.group_hr_holidays_user', kind=None)],
                                                            keywords=[],
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
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Choose the Time Off Officer who will be notified to approve allocation or Time Off request', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='leave_validation_type', ctx=Store())],
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
                                            Constant(value='no_validation', kind=None),
                                            Constant(value='No Validation', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='hr', kind=None),
                                            Constant(value='By Time Off Officer', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='manager', kind=None),
                                            Constant(value="By Employee's Approver", kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='both', kind=None),
                                            Constant(value="By Employee's Approver and Time Off Officer", kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='hr', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Leave Validation', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='requires_allocation', ctx=Store())],
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
                                            Constant(value='yes', kind=None),
                                            Constant(value='Yes', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='no', kind=None),
                                            Constant(value='No Limit', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='yes', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Requires allocation', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='employee_requests', ctx=Store())],
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
                                            Constant(value='yes', kind=None),
                                            Constant(value='Extra Days Requests Allowed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='no', kind=None),
                                            Constant(value='Not Allowed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='no', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Employee Requests', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='allocation_validation_type', ctx=Store())],
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
                                            Constant(value='no', kind=None),
                                            Constant(value='No validation needed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='officer', kind=None),
                                            Constant(value='Approved by Time Off Officer', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='set', kind=None),
                                            Constant(value='Set by Time Off Officer', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='officer', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Approval', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='has_valid_allocation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_valid', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_valid', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This indicates if it is still possible to use this type of leave', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='time_type', ctx=Store())],
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
                                            Constant(value='leave', kind=None),
                                            Constant(value='Time Off', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='other', kind=None),
                                            Constant(value='Other', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='leave', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Kind of Leave', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Whether this should be computed as a holiday or as work time (eg: formation)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='request_unit', ctx=Store())],
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
                                            Constant(value='day', kind=None),
                                            Constant(value='Day', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='half_day', kind=None),
                                            Constant(value='Half Day', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='hour', kind=None),
                                            Constant(value='Hours', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='day', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Take Time Off in', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='unpaid', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is Unpaid', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='leave_notif_subtype_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mail.message.subtype', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Time Off Notification Subtype', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='hr_holidays.mt_leave', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_not_found',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='allocation_notif_subtype_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mail.message.subtype', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Allocation Notification Subtype', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='hr_holidays.mt_leave_allocation', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_not_found',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='support_document', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Supporting Document', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='accruals_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='hr.leave.accrual.plan', kind=None),
                            Constant(value='time_off_type_id', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='accrual_count', ctx=Store())],
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
                                value=Constant(value='_compute_accrual_count', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Accruals count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_valid',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Returns leave_type ids for which a valid allocation exists\n            or that don't need an allocation\n            return [('id', domain_operator, [x['id'] for x in res])]\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='date_to', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
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
                                        args=[Constant(value='default_date_from', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='today',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='%Y-1-1', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_from', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
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
                                        args=[Constant(value='default_date_to', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='today',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='%Y-12-31', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='value', ctx=Load()),
                                        Name(id='bool', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Invalid value: %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='value', ctx=Load()),
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
                                left=Name(id='operator', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='=', kind=None),
                                            Constant(value='!=', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Invalid operator: %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='operator', ctx=Load()),
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
                            targets=[Name(id='new_operator', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='operator', ctx=Load()),
                                    ops=[Eq()],
                                    comparators=[Constant(value='=', kind=None)],
                                ),
                                body=Constant(value='in', kind=None),
                                orelse=Constant(value='not in', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value='\n        SELECT\n            holiday_status_id\n        FROM\n            hr_leave_allocation alloc\n        WHERE\n            alloc.date_to >= %s OR alloc.date_to IS NULL AND\n            alloc.date_from <= %s \n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='query', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='date_to', ctx=Load()),
                                            Name(id='date_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Name(id='new_operator', ctx=Load()),
                                            ListComp(
                                                elt=Subscript(
                                                    value=Name(id='x', ctx=Load()),
                                                    slice=Constant(value='holiday_status_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dictfetchall',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
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
                    name='_compute_valid',
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
                            targets=[Name(id='date_to', ctx=Store())],
                            value=Call(
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
                                    Constant(value='default_date_to', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='today',
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
                            targets=[Name(id='date_from', ctx=Store())],
                            value=Call(
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
                                    Constant(value='default_date_from', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='today',
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
                        For(
                            target=Name(id='holiday_type', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='holiday_type', ctx=Load()),
                                        attr='requires_allocation',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='allocation', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='hr.leave.allocation', kind=None),
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
                                                                    Constant(value='holiday_status_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='holiday_type', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='|', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='date_to', kind=None),
                                                                    Constant(value='>=', kind=None),
                                                                    Name(id='date_to', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='&', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='date_to', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='date_from', kind=None),
                                                                    Constant(value='<=', kind=None),
                                                                    Name(id='date_from', ctx=Load()),
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
                                                    value=Name(id='holiday_type', ctx=Load()),
                                                    attr='has_valid_allocation',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[Name(id='allocation', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='holiday_type', ctx=Load()),
                                                    attr='has_valid_allocation',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
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
                            args=[Constant(value='requires_allocation', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_max_leaves',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Name(id='float', ctx=Load()),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employee_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_contextual_employee_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='int', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='employee_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='allocations', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='hr.leave.allocation', kind=None),
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
                                                            Constant(value='employee_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='employee_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='validate', kind=None),
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
                                    target=Name(id='allocation', ctx=Store()),
                                    iter=Name(id='allocations', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='leaves', ctx=Load()),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='allocation', ctx=Load()),
                                                        attr='holiday_status_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Attribute(
                                                value=Name(id='allocation', ctx=Load()),
                                                attr='number_of_days',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='valid_leave', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='leave', ctx=Store()),
                            iter=Name(id='leaves', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='operator', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='>', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='leaves', ctx=Load()),
                                                    slice=Name(id='leave', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[Name(id='value', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='valid_leave', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='leave', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='operator', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='<', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='leaves', ctx=Load()),
                                                            slice=Name(id='leave', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Lt()],
                                                        comparators=[Name(id='value', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='valid_leave', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='leave', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='operator', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='=', kind=None)],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Name(id='leaves', ctx=Load()),
                                                                    slice=Name(id='leave', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='value', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='valid_leave', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='leave', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='operator', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='!=', kind=None)],
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='leaves', ctx=Load()),
                                                                            slice=Name(id='leave', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[NotEq()],
                                                                        comparators=[Name(id='value', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='valid_leave', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='leave', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='in', kind=None),
                                            Name(id='valid_leave', ctx=Load()),
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
                    name='_search_virtual_remaining_leaves',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Name(id='float', ctx=Load()),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave_types', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.leave.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='valid_leave_types', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='hr.leave.type', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='leave_type', ctx=Store()),
                            iter=Name(id='leave_types', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='leave_type', ctx=Load()),
                                            attr='requires_allocation',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='yes', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='operator', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='>', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='leave_type', ctx=Load()),
                                                            attr='virtual_remaining_leaves',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Name(id='value', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='valid_leave_types', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Name(id='leave_type', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='operator', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='<', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='leave_type', ctx=Load()),
                                                                    attr='virtual_remaining_leaves',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Lt()],
                                                                comparators=[Name(id='value', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='valid_leave_types', ctx=Store()),
                                                            op=BitOr(),
                                                            value=Name(id='leave_type', ctx=Load()),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='operator', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='>=', kind=None)],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='leave_type', ctx=Load()),
                                                                            attr='virtual_remaining_leaves',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[GtE()],
                                                                        comparators=[Name(id='value', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='valid_leave_types', ctx=Store()),
                                                                    op=BitOr(),
                                                                    value=Name(id='leave_type', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='operator', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='<=', kind=None)],
                                                                            ),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='leave_type', ctx=Load()),
                                                                                    attr='virtual_remaining_leaves',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[LtE()],
                                                                                comparators=[Name(id='value', ctx=Load())],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Name(id='valid_leave_types', ctx=Store()),
                                                                            op=BitOr(),
                                                                            value=Name(id='leave_type', ctx=Load()),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Compare(
                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='=', kind=None)],
                                                                                    ),
                                                                                    Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='leave_type', ctx=Load()),
                                                                                            attr='virtual_remaining_leaves',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Name(id='value', ctx=Load())],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                AugAssign(
                                                                                    target=Name(id='valid_leave_types', ctx=Store()),
                                                                                    op=BitOr(),
                                                                                    value=Name(id='leave_type', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='!=', kind=None)],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='leave_type', ctx=Load()),
                                                                                                    attr='virtual_remaining_leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[NotEq()],
                                                                                                comparators=[Name(id='value', ctx=Load())],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        AugAssign(
                                                                                            target=Name(id='valid_leave_types', ctx=Store()),
                                                                                            op=BitOr(),
                                                                                            value=Name(id='leave_type', ctx=Load()),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Name(id='valid_leave_types', ctx=Store()),
                                            op=BitOr(),
                                            value=Name(id='leave_type', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='valid_leave_types', ctx=Load()),
                                                attr='ids',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_employees_days',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='employee_ids', annotation=None, type_comment=None),
                            arg(arg='date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=DictComp(
                                key=Name(id='employee_id', ctx=Load()),
                                value=DictComp(
                                    key=Attribute(
                                        value=Name(id='leave_type', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    value=Dict(
                                        keys=[
                                            Constant(value='max_leaves', kind=None),
                                            Constant(value='leaves_taken', kind=None),
                                            Constant(value='remaining_leaves', kind=None),
                                            Constant(value='virtual_remaining_leaves', kind=None),
                                            Constant(value='virtual_leaves_taken', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='leave_type', ctx=Store()),
                                            iter=Name(id='self', ctx=Load()),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='employee_id', ctx=Store()),
                                        iter=Name(id='employee_ids', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='requests', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.leave', kind=None),
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
                                                    Constant(value='employee_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='employee_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='confirm', kind=None),
                                                            Constant(value='validate1', kind=None),
                                                            Constant(value='validate', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='holiday_status_id', kind=None),
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='date', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='date', ctx=Store())],
                                    value=Call(
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='allocations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.leave.allocation', kind=None),
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
                                                    Constant(value='employee_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='employee_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='confirm', kind=None),
                                                            Constant(value='validate1', kind=None),
                                                            Constant(value='validate', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='holiday_status_id', kind=None),
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
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='date', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_to', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_to', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Name(id='date', ctx=Load()),
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
                            target=Name(id='request', ctx=Store()),
                            iter=Name(id='requests', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='status_dict', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='employee_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='holiday_status_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
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
                                                operand=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='holiday_allocation_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='holiday_allocation_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='allocations', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='status_dict', ctx=Load()),
                                                slice=Constant(value='virtual_remaining_leaves', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Sub(),
                                            value=IfExp(
                                                test=Compare(
                                                    left=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='leave_type_request_unit',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='hour', kind=None)],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='number_of_hours_display',
                                                    ctx=Load(),
                                                ),
                                                orelse=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='number_of_days',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='holiday_status_id',
                                                ctx=Load(),
                                            ),
                                            attr='requires_allocation',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='no', kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='status_dict', ctx=Load()),
                                                slice=Constant(value='virtual_leaves_taken', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=IfExp(
                                                test=Compare(
                                                    left=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='leave_type_request_unit',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='hour', kind=None)],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='number_of_hours_display',
                                                    ctx=Load(),
                                                ),
                                                orelse=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='number_of_days',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='validate', kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='status_dict', ctx=Load()),
                                                        slice=Constant(value='leaves_taken', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=IfExp(
                                                        test=Compare(
                                                            left=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='leave_type_request_unit',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='hour', kind=None)],
                                                        ),
                                                        body=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='number_of_hours_display',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='number_of_days',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='status_dict', ctx=Load()),
                                                        slice=Constant(value='remaining_leaves', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Sub(),
                                                    value=IfExp(
                                                        test=Compare(
                                                            left=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='leave_type_request_unit',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='hour', kind=None)],
                                                        ),
                                                        body=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='number_of_hours_display',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='number_of_days',
                                                            ctx=Load(),
                                                        ),
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
                            target=Name(id='allocation', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='allocations', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='status_dict', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Attribute(
                                                value=Attribute(
                                                    value=Name(id='allocation', ctx=Load()),
                                                    attr='employee_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='allocation', ctx=Load()),
                                                attr='holiday_status_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='allocation', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='validate', kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='status_dict', ctx=Load()),
                                                slice=Constant(value='virtual_remaining_leaves', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=IfExp(
                                                test=Compare(
                                                    left=Attribute(
                                                        value=Name(id='allocation', ctx=Load()),
                                                        attr='type_request_unit',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='hour', kind=None)],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='allocation', ctx=Load()),
                                                    attr='number_of_hours_display',
                                                    ctx=Load(),
                                                ),
                                                orelse=Attribute(
                                                    value=Name(id='allocation', ctx=Load()),
                                                    attr='number_of_days',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='allocation', ctx=Load()),
                                                        attr='holiday_status_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='requires_allocation',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='no', kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='status_dict', ctx=Load()),
                                                        slice=Constant(value='max_leaves', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=IfExp(
                                                        test=Compare(
                                                            left=Attribute(
                                                                value=Name(id='allocation', ctx=Load()),
                                                                attr='type_request_unit',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='hour', kind=None)],
                                                        ),
                                                        body=Attribute(
                                                            value=Name(id='allocation', ctx=Load()),
                                                            attr='number_of_hours_display',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Attribute(
                                                            value=Name(id='allocation', ctx=Load()),
                                                            attr='number_of_days',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='status_dict', ctx=Load()),
                                                        slice=Constant(value='remaining_leaves', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=IfExp(
                                                        test=Compare(
                                                            left=Attribute(
                                                                value=Name(id='allocation', ctx=Load()),
                                                                attr='type_request_unit',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='hour', kind=None)],
                                                        ),
                                                        body=Attribute(
                                                            value=Name(id='allocation', ctx=Load()),
                                                            attr='number_of_hours_display',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Attribute(
                                                            value=Name(id='allocation', ctx=Load()),
                                                            attr='number_of_days',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='remaining_leaves', ctx=Store())],
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='allocation', ctx=Load()),
                                                            attr='max_leaves',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='allocation', ctx=Load()),
                                                            attr='leaves_taken',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='status_dict', ctx=Load()),
                                                        slice=Constant(value='max_leaves', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Attribute(
                                                        value=Name(id='allocation', ctx=Load()),
                                                        attr='max_leaves',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='status_dict', ctx=Load()),
                                                        slice=Constant(value='remaining_leaves', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Name(id='remaining_leaves', ctx=Load()),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='status_dict', ctx=Load()),
                                                        slice=Constant(value='leaves_taken', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Attribute(
                                                        value=Name(id='allocation', ctx=Load()),
                                                        attr='leaves_taken',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
                    name='get_days_all_request',
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
                            targets=[Name(id='leave_types', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[List(elts=[], ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
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
                                                    op=Or(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='virtual_remaining_leaves',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Gt()],
                                                            comparators=[Constant(value=0, kind=None)],
                                                        ),
                                                        Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='max_leaves',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_model_sorting_key',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='reverse',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='lt', ctx=Load()),
                                        attr='_get_days_request',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='lt', ctx=Store()),
                                        iter=Name(id='leave_types', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
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
                    name='_get_days_request',
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
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='remaining_leaves', kind=None),
                                            Constant(value='virtual_remaining_leaves', kind=None),
                                            Constant(value='max_leaves', kind=None),
                                            Constant(value='leaves_taken', kind=None),
                                            Constant(value='virtual_leaves_taken', kind=None),
                                            Constant(value='request_unit', kind=None),
                                            Constant(value='icon', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Constant(value='%.2f', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='remaining_leaves',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            attr='rstrip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='0', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='rstrip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Constant(value='%.2f', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='virtual_remaining_leaves',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            attr='rstrip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='0', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='rstrip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Constant(value='%.2f', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='max_leaves',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            attr='rstrip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='0', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='rstrip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Constant(value='%.2f', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='leaves_taken',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            attr='rstrip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='0', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='rstrip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Constant(value='%.2f', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='virtual_leaves_taken',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            attr='rstrip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='0', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='rstrip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='request_unit',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='icon_id',
                                                    ctx=Load(),
                                                ),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='requires_allocation',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
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
                    name='_get_contextual_employee_id',
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
                                left=Constant(value='employee_id', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='employee_id', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='employee_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Constant(value='default_employee_id', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='employee_id', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='default_employee_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='employee_id', ctx=Store())],
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
                                                    attr='employee_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='employee_id', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_leaves',
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
                            targets=[Name(id='data_days', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employee_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_contextual_employee_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='employee_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='data_days', ctx=Store())],
                                    value=IfExp(
                                        test=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='employee_id', ctx=Load()),
                                                Name(id='list', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        body=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_employees_days',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='employee_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            slice=Subscript(
                                                value=Name(id='employee_id', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        orelse=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_employees_days',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Name(id='employee_id', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Name(id='employee_id', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='holiday_status', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data_days', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='holiday_status', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='holiday_status', ctx=Load()),
                                            attr='max_leaves',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='max_leaves', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='holiday_status', ctx=Load()),
                                            attr='leaves_taken',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='leaves_taken', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='holiday_status', ctx=Load()),
                                            attr='remaining_leaves',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='remaining_leaves', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='holiday_status', ctx=Load()),
                                            attr='virtual_remaining_leaves',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='virtual_remaining_leaves', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='holiday_status', ctx=Load()),
                                            attr='virtual_leaves_taken',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='virtual_leaves_taken', kind=None),
                                            Constant(value=0, kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_group_days_allocation',
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
                            targets=[Name(id='date_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='month',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='day',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='hour',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='minute',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='second',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='microsecond',
                                                value=Constant(value=0, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_from', kind=None),
                                            Constant(value='>=', kind=None),
                                            Name(id='date_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_from', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='grouped_res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.leave.allocation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[Constant(value='holiday_status_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='holiday_status_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='grouped_dict', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='holiday_status_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='data', ctx=Load()),
                                                    slice=Constant(value='holiday_status_id_count', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='data', ctx=Store()),
                                                iter=Name(id='grouped_res', ctx=Load()),
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
                        For(
                            target=Name(id='allocation', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='allocation', ctx=Load()),
                                            attr='group_days_allocation',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='grouped_dict', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='allocation', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_group_days_leave',
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
                            targets=[Name(id='grouped_res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.leave', kind=None),
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
                                                    Constant(value='holiday_status_id', kind=None),
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
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='datetime', ctx=Load()),
                                                                                attr='datetime',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='now',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='month',
                                                                        value=Constant(value=1, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='day',
                                                                        value=Constant(value=1, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='hour',
                                                                        value=Constant(value=0, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='minute',
                                                                        value=Constant(value=0, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='second',
                                                                        value=Constant(value=0, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='microsecond',
                                                                        value=Constant(value=0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='holiday_status_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='holiday_status_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='grouped_dict', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='holiday_status_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='data', ctx=Load()),
                                                    slice=Constant(value='holiday_status_id_count', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='data', ctx=Store()),
                                                iter=Name(id='grouped_res', ctx=Load()),
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
                        For(
                            target=Name(id='allocation', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='allocation', ctx=Load()),
                                            attr='group_days_leave',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='grouped_dict', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='allocation', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_accrual_count',
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
                            targets=[Name(id='accrual_allocations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.leave.accrual.plan', kind=None),
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
                                                    Constant(value='time_off_type_id', kind=None),
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
                                        elts=[Constant(value='time_off_type_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='time_off_type_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapped_data', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='time_off_type_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='data', ctx=Load()),
                                                    slice=Constant(value='time_off_type_id_count', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='data', ctx=Store()),
                                                iter=Name(id='accrual_allocations', ctx=Load()),
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
                        For(
                            target=Name(id='leave_type', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='leave_type', ctx=Load()),
                                            attr='accrual_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mapped_data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='leave_type', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
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
                    decorator_list=[],
                    returns=None,
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='employee_id', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='HolidaysType', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='name_get',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='requires_allocation',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='yes', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%(name)s (%(count)s)', kind=None),
                                                op=Mod(),
                                                right=Dict(
                                                    keys=[
                                                        Constant(value='name', kind=None),
                                                        Constant(value='count', kind=None),
                                                    ],
                                                    values=[
                                                        Name(id='name', ctx=Load()),
                                                        BinOp(
                                                            left=BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='%g remaining out of %g', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Call(
                                                                                    func=Name(id='float_round', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='record', ctx=Load()),
                                                                                            attr='virtual_remaining_leaves',
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
                                                                                Constant(value=0.0, kind=None),
                                                                            ],
                                                                        ),
                                                                        BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Call(
                                                                                    func=Name(id='float_round', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='record', ctx=Load()),
                                                                                            attr='max_leaves',
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
                                                                                Constant(value=0.0, kind=None),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=IfExp(
                                                                test=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='request_unit',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='hour', kind=None)],
                                                                ),
                                                                body=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value=' hours', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                orelse=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value=' days', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='name', ctx=Load()),
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
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='count', annotation=None, type_comment=None),
                            arg(arg='access_rights_uid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override _search to order the results, according to some employee.\n        The order is the following\n\n         - allocation fixed first, then allowing allocation, then free allocation\n         - virtual remaining leaves (higher the better, so using reverse on sorted)\n\n        This override is necessary because those fields are not stored and depends\n        on an employee_id given in context. This sort will be done when there\n        is an employee_id in context and that no other order has been given\n        to the method.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='employee_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_contextual_employee_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='post_sort', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='count', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='order', ctx=Load()),
                                    ),
                                    Name(id='employee_id', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='HolidaysType', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=IfExp(
                                            test=Name(id='post_sort', ctx=Load()),
                                            body=Constant(value=None, kind=None),
                                            orelse=Name(id='limit', ctx=Load()),
                                        ),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Name(id='order', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='count',
                                        value=Name(id='count', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='access_rights_uid',
                                        value=Name(id='access_rights_uid', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='leave_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='post_sort', ctx=Load()),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='leaves', ctx=Load()),
                                                    attr='sorted',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='key',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_model_sorting_key',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='reverse',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='limit', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='leave_ids', ctx=Load()),
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
                    name='action_see_days_allocated',
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
                                args=[Constant(value='hr_holidays.hr_leave_allocation_action_all', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='month',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='day',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='hour',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='minute',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='second',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='microsecond',
                                                value=Constant(value=0, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
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
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_from', kind=None),
                                            Constant(value='>=', kind=None),
                                            Name(id='date_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_from', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
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
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='default_holiday_type', kind=None),
                                    Constant(value='default_holiday_status_id', kind=None),
                                ],
                                values=[
                                    Constant(value='department', kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                    name='action_see_group_leaves',
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
                                args=[Constant(value='hr_holidays.hr_leave_action_action_approve_department', kind=None)],
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
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_from', kind=None),
                                            Constant(value='>=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='datetime', ctx=Load()),
                                                                        attr='datetime',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='now',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='month',
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='day',
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='hour',
                                                                value=Constant(value=0, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='minute',
                                                                value=Constant(value=0, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='second',
                                                                value=Constant(value=0, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='microsecond',
                                                                value=Constant(value=0, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
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
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='default_holiday_status_id', kind=None)],
                                values=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                    name='action_see_accrual_plans',
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
                                args=[Constant(value='hr_holidays.open_view_accrual_plans', kind=None)],
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
                                            Constant(value='time_off_type_id', kind=None),
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
                            value=Dict(
                                keys=[Constant(value='default_time_off_type_id', kind=None)],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
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
