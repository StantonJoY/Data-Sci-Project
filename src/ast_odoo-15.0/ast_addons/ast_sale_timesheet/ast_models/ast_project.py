Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
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
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='ValidationError', asname=None),
                alias(name='UserError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='format_amount', asname=None),
                alias(name='float_is_zero', asname=None),
                alias(name='formatLang', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Project',
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
                    value=Constant(value='project.project', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Pre-fill timesheet product as "Time" data product when creating new project allowing billable tasks by default. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Project', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='timesheet_product_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields', ctx=Load())],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='allow_billable', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='allow_timesheets', kind=None)],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='result', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='timesheet_product_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='default_product', ctx=Store())],
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
                                        args=[
                                            Constant(value='sale_timesheet.time_product', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='default_product', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='timesheet_product_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='default_product', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                    name='_default_timesheet_product_id',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='sale_timesheet.time_product', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pricing_type', ctx=Store())],
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
                                            Constant(value='task_rate', kind=None),
                                            Constant(value='Task rate', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='fixed_rate', kind=None),
                                            Constant(value='Project rate', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='employee_rate', kind=None),
                                            Constant(value='Employee rate', kind=None),
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
                                value=Constant(value='Pricing', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='task_rate', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_pricing_type', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_pricing_type', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The task rate is perfect if you would like to bill different services to different customers at different rates. The fixed rate is perfect if you bill a service at a fixed rate per hour or day worked regardless of the employee who performed it. The employee rate is preferable if your employees deliver the same service at a different rate. For instance, junior and senior consultants would deliver the same service (= consultancy), but at a different rate because of their level of seniority.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sale_line_employee_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='project.sale.line.employee.map', kind=None),
                            Constant(value='project_id', kind=None),
                            Constant(value='Sale line/Employee map', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Employee/Sale Order Item Mapping:\n Defines to which sales order item an employee's timesheet entry will be linked.By extension, it defines the rate at which an employee's time on the project is billed.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='allow_billable', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Billable', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Invoice your time and material from tasks.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='billable_percentage', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_billable_percentage', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='% of timesheets that are billable compared to the total number of timesheets linked to the AA of the project, rounded to the unit.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='display_create_order', ctx=Store())],
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
                                value=Constant(value='_compute_display_create_order', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='timesheet_product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.product', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Timesheet Product', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[\n            ('detailed_type', '=', 'service'),\n            ('invoice_policy', '=', 'delivery'),\n            ('service_type', '=', 'timesheet'),\n            '|', ('company_id', '=', False), ('company_id', '=', company_id)]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Select a Service product with which you would like to bill your time spent on tasks.', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_timesheet_product_id', kind=None),
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
                                arg='default',
                                value=Name(id='_default_timesheet_product_id', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='warning_employee_rate', ctx=Store())],
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
                                value=Constant(value='_compute_warning_employee_rate', kind=None),
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
                    name='_compute_pricing_type',
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
                            targets=[Name(id='billable_projects', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='allow_billable', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='project', ctx=Store()),
                            iter=Name(id='billable_projects', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='sale_line_employee_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='project', ctx=Load()),
                                                    attr='pricing_type',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='employee_rate', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='sale_line_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='pricing_type',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='fixed_rate', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='pricing_type',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='task_rate', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Name(id='self', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='billable_projects', ctx=Load()),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='pricing_type', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                Constant(value='sale_line_id', kind=None),
                                Constant(value='sale_line_employee_ids', kind=None),
                                Constant(value='allow_billable', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_pricing_type',
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
                            value=Constant(value=" Search method for pricing_type field.\n\n            This method returns a domain based on the operator and the value given in parameter:\n            - operator = '=':\n                - value = 'task_rate': [('sale_line_employee_ids', '=', False), ('sale_line_id', '=', False), ('allow_billable', '=', True)]\n                - value = 'fixed_rate': [('sale_line_employee_ids', '=', False), ('sale_line_id', '!=', False), ('allow_billable', '=', True)]\n                - value = 'employee_rate': [('sale_line_employee_ids', '!=', False), ('allow_billable', '=', True)]\n                - value is False: [('allow_billable', '=', False)]\n            - operator = '!=':\n                - value = 'task_rate': ['|', ('sale_line_employee_ids', '!=', False), ('sale_line_id', '!=', False), ('allow_billable', '=', True)]\n                - value = 'fixed_rate': ['|', ('sale_line_employee_ids', '!=', False), ('sale_line_id', '=', False), ('allow_billable', '=', True)]\n                - value = 'employee_rate': [('sale_line_employee_ids', '=', False), ('allow_billable', '=', True)]\n                - value is False: [('allow_billable', '!=', False)]\n\n            :param operator: the supported operator is either '=' or '!='.\n            :param value: the value than the field should be is among these values into the following tuple: (False, 'task_rate', 'fixed_rate', 'employee_rate').\n\n            :returns: the domain to find the expected projects.\n        ", kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='operator', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Tuple(
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
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Operation not supported', kind=None)],
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=Or(),
                                    values=[
                                        BoolOp(
                                            op=And(),
                                            values=[
                                                Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='value', ctx=Load()),
                                                        Name(id='bool', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Compare(
                                                    left=Name(id='value', ctx=Load()),
                                                    ops=[Is()],
                                                    comparators=[Constant(value=False, kind=None)],
                                                ),
                                            ],
                                        ),
                                        BoolOp(
                                            op=And(),
                                            values=[
                                                Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='value', ctx=Load()),
                                                        Name(id='str', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Compare(
                                                    left=Name(id='value', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='task_rate', kind=None),
                                                                Constant(value='fixed_rate', kind=None),
                                                                Constant(value='employee_rate', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Value does not exist in the pricing type', kind=None)],
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
                        If(
                            test=Compare(
                                left=Name(id='value', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=False, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='allow_billable', kind=None),
                                                    Name(id='operator', ctx=Load()),
                                                    Name(id='value', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='sol_cond', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='sale_line_id', kind=None),
                                    Constant(value='!=', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapping_cond', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='sale_line_employee_ids', kind=None),
                                    Constant(value='!=', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='value', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='task_rate', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='expression', ctx=Load()),
                                                attr='NOT_OPERATOR',
                                                ctx=Load(),
                                            ),
                                            Name(id='sol_cond', ctx=Load()),
                                            Attribute(
                                                value=Name(id='expression', ctx=Load()),
                                                attr='NOT_OPERATOR',
                                                ctx=Load(),
                                            ),
                                            Name(id='mapping_cond', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='value', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='fixed_rate', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Name(id='sol_cond', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='expression', ctx=Load()),
                                                        attr='NOT_OPERATOR',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='mapping_cond', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Name(id='sol_cond', ctx=Load()),
                                                    Name(id='mapping_cond', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='normalize_domain',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='operator', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='=', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='insert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Name(id='expression', ctx=Load()),
                                                attr='NOT_OPERATOR',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='distribute_not',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
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
                                                            Constant(value='allow_billable', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
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
                        Return(
                            value=Name(id='domain', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_billable_percentage',
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
                            targets=[Name(id='timesheets_read_group', ctx=Store())],
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
                                            Constant(value='project_id', kind=None),
                                            Constant(value='so_line', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='project_id', kind=None),
                                            Constant(value='so_line', kind=None),
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
                            targets=[Name(id='timesheets_by_project', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='res', ctx=Store()),
                            iter=Name(id='timesheets_read_group', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='timesheets_by_project', ctx=Load()),
                                                slice=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='project_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='unit_amount', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='bool', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Constant(value='so_line', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
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
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='project', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='timesheet_total', ctx=Store()),
                                        Name(id='timesheet_billable', ctx=Store()),
                                    ],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='unit_amount', ctx=Store()),
                                            Name(id='is_billable_timesheet', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Subscript(
                                        value=Name(id='timesheets_by_project', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='timesheet_total', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='unit_amount', ctx=Load()),
                                        ),
                                        If(
                                            test=Name(id='is_billable_timesheet', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='timesheet_billable', ctx=Store()),
                                                    op=Add(),
                                                    value=Name(id='unit_amount', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='billable_percentage', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='timesheet_total', ctx=Load()),
                                            ops=[Gt()],
                                            comparators=[Constant(value=0, kind=None)],
                                        ),
                                        body=BinOp(
                                            left=BinOp(
                                                left=Name(id='timesheet_billable', ctx=Load()),
                                                op=Div(),
                                                right=Name(id='timesheet_total', ctx=Load()),
                                            ),
                                            op=Mult(),
                                            right=Constant(value=100, kind=None),
                                        ),
                                        orelse=Constant(value=0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='billable_percentage',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[Name(id='billable_percentage', ctx=Load())],
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
                                Constant(value='analytic_account_id', kind=None),
                                Constant(value='timesheet_ids', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_display_create_order',
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
                            target=Name(id='project', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='display_create_order',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='project', ctx=Load()),
                                                    attr='pricing_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='task_rate', kind=None)],
                                            ),
                                        ],
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
                                Constant(value='partner_id', kind=None),
                                Constant(value='pricing_type', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_timesheet_product_id',
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
                            targets=[Name(id='default_product', ctx=Store())],
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
                                args=[
                                    Constant(value='sale_timesheet.time_product', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='project', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='project', ctx=Load()),
                                                    attr='allow_timesheets',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='project', ctx=Load()),
                                                    attr='allow_billable',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='project', ctx=Load()),
                                                    attr='timesheet_product_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='project', ctx=Load()),
                                                    attr='timesheet_product_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='timesheet_product_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='default_product', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
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
                            args=[
                                Constant(value='allow_timesheets', kind=None),
                                Constant(value='allow_billable', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_warning_employee_rate',
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
                            targets=[Name(id='projects', ctx=Store())],
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
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
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
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='allow_billable',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='allow_timesheets',
                                                    ctx=Load(),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='pricing_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='employee_rate', kind=None)],
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
                            targets=[Name(id='employees', ctx=Store())],
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
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='task_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='projects', ctx=Load()),
                                                            attr='task_ids',
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
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='project_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='project_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='project_id', kind=None),
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
                            targets=[Name(id='dict_project_employee', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='employees', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='dict_project_employee', ctx=Load()),
                                        slice=Subscript(
                                            value=Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Constant(value='project_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=IfExp(
                                        test=Subscript(
                                            value=Name(id='line', ctx=Load()),
                                            slice=Constant(value='employee_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        body=List(
                                            elts=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Constant(value='employee_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        orelse=List(elts=[], ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='project', ctx=Store()),
                            iter=Name(id='projects', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='warning_employee_rate',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='x', ctx=Load()),
                                                    ops=[NotIn()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='project', ctx=Load()),
                                                                    attr='sale_line_employee_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='employee_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Subscript(
                                                            value=Name(id='dict_project_employee', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='project', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=BinOp(
                                        left=Name(id='self', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='projects', ctx=Load()),
                                    ),
                                    attr='warning_employee_rate',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
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
                                Constant(value='pricing_type', kind=None),
                                Constant(value='allow_timesheets', kind=None),
                                Constant(value='allow_billable', kind=None),
                                Constant(value='sale_line_employee_ids', kind=None),
                                Constant(value='sale_line_employee_ids.employee_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
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
                            target=Name(id='project', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='allow_billable',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='allow_timesheets',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='project', ctx=Load()),
                                                    attr='pricing_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='task_rate', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sol', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='project', ctx=Load()),
                                                        attr='sale_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='project', ctx=Load()),
                                                                attr='sale_line_employee_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='sale_line_id',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Slice(
                                                            lower=None,
                                                            upper=Constant(value=1, kind=None),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='project', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='sol', ctx=Load()),
                                                attr='order_partner_id',
                                                ctx=Load(),
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
                                Constant(value='sale_line_employee_ids.sale_line_id', kind=None),
                                Constant(value='sale_line_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_sale_line_id',
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
                                    attr='_compute_sale_line_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='project', ctx=Store()),
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
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
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
                                                    operand=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='sale_line_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='pricing_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='employee_rate', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sol', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='is_service', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='order_partner_id', kind=None),
                                                            Constant(value='child_of', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='project', ctx=Load()),
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='is_expense', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='in', kind=None),
                                                            List(
                                                                elts=[
                                                                    Constant(value='sale', kind=None),
                                                                    Constant(value='done', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='remaining_hours', kind=None),
                                                            Constant(value='>', kind=None),
                                                            Constant(value=0, kind=None),
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
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='sale_line_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='sol', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='project', ctx=Load()),
                                                        attr='sale_line_employee_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sale_line_id',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=1, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
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
                            args=[Constant(value='partner_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_sale_line_type',
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
                            target=Name(id='project', ctx=Store()),
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
                                            args=[arg(arg='project', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='sale_line_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='sale_line_id',
                                                ctx=Load(),
                                            ),
                                            attr='is_service',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You cannot link a billable project to a sales order item that is not a service.', kind=None)],
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
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='project', ctx=Load()),
                                            attr='sale_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='is_expense',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You cannot link a billable project to a sales order item that comes from an expense or a vendor bill.', kind=None)],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='sale_line_id', kind=None)],
                            keywords=[],
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Project', ctx=Load()),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='allow_billable', kind=None),
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
                                            args=[Constant(value='allow_billable', kind=None)],
                                            keywords=[],
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
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='task_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_timesheet',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='so_line', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                    name='_update_timesheets_sale_line_id',
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
                            target=Name(id='project', ctx=Store()),
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
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
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
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='allow_billable',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='allow_timesheets',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='timesheet_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=False, kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='timesheet_ids', kind=None)],
                                                keywords=[],
                                            ),
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
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='t', ctx=Load()),
                                                                attr='is_so_line_edited',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='t', ctx=Load()),
                                                                attr='_is_not_billed',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='timesheet_ids', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='employee_id', ctx=Store()),
                                    iter=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='project', ctx=Load()),
                                                    attr='sale_line_employee_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Name(id='l', ctx=Load()),
                                                            attr='project_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='project', ctx=Load())],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='employee_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sale_line_id', ctx=Store())],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='sale_line_employee_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='filtered',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='l', ctx=Load()),
                                                                            attr='project_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='project', ctx=Load())],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='l', ctx=Load()),
                                                                            attr='employee_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='employee_id', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='sale_line_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='timesheet_ids', ctx=Load()),
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
                                                                        body=Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='t', ctx=Load()),
                                                                                attr='employee_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Name(id='employee_id', ctx=Load())],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='so_line',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='sale_line_id', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                    name='action_open_project_invoices',
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
                            targets=[Name(id='invoices', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='line_ids.analytic_account_id', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='line_ids.analytic_account_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='analytic_account_id',
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
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='out_invoice', kind=None),
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
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='views', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Invoices', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='account.move', kind=None),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='kanban', kind=None),
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
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='invoices', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='create', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='invoices', ctx=Load())],
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
                                            List(
                                                elts=[
                                                    Constant(value=False, kind=None),
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
                                        value=Name(id='invoices', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                    name='action_view_timesheet',
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
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='view_id', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='help', kind=None),
                                    Constant(value='limit', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='Timesheets of %s', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='account.analytic.line', kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value='tree,form', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='\n                <p class="o_view_nocontent_smiling_face">\n                    Record timesheets\n                </p><p>\n                    You can register and track your workings hours by project every\n                    day. Every time spent on a project will become a cost and can be re-invoiced to\n                    customers if required.\n                </p>\n            ', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=80, kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='default_project_id', kind=None),
                                            Constant(value='search_default_project_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='action_make_billable',
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
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='views', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Create Sales Order', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='project.create.sale.order', kind=None),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='new', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='active_id', kind=None),
                                            Constant(value='active_model', kind=None),
                                            Constant(value='default_product_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='project.project', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='timesheet_product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='action_billable_time_button',
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
                                args=[Constant(value='hr_timesheet.timesheet_action_all', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                            Constant(value='context', kind=None),
                                            Constant(value='domain', kind=None),
                                            Constant(value='view_mode', kind=None),
                                            Constant(value='views', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='search_default_groupby_task', kind=None),
                                                    Constant(value='default_project_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='project_id', kind=None),
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
                                            Constant(value='tree,kanban,pivot,graph,form', kind=None),
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
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
                                                                    args=[Constant(value='hr_timesheet.timesheet_view_tree_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='tree', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
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
                                                                    args=[Constant(value='hr_timesheet.view_kanban_account_analytic_line', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='kanban', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
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
                                                                    args=[Constant(value='hr_timesheet.view_hr_timesheet_line_pivot', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='pivot', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
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
                                                                    args=[Constant(value='hr_timesheet.view_hr_timesheet_line_graph_all', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='graph', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
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
                                                                    args=[Constant(value='hr_timesheet.timesheet_view_form_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                    name='action_view_all_rating',
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
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='view_type', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='domain', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Rating', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='rating.rating', kind=None),
                                    Constant(value='kanban,list,graph,pivot,form', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Dict(
                                        keys=[Constant(value='search_default_rating_last_30_days', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='consumed', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='parent_res_model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='project.project', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='parent_res_id', kind=None),
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
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_panel_data',
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
                            targets=[Name(id='panel_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Project', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_panel_data',
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
                                    None,
                                    Constant(value='analytic_account_id', kind=None),
                                    Constant(value='sold_items', kind=None),
                                    Constant(value='profitability_items', kind=None),
                                ],
                                values=[
                                    Name(id='panel_data', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='analytic_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_sold_items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_profitability_items',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                    name='_get_sale_order_lines',
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
                            targets=[Name(id='sale_orders', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sale_order_id',
                                    ctx=Load(),
                                ),
                                op=BitOr(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tasks',
                                        ctx=Load(),
                                    ),
                                    attr='sale_order_id',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
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
                                                    Attribute(
                                                        value=Name(id='sale_orders', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='is_service', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id asc', kind=None),
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
                    name='_get_sold_items',
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
                            targets=[Name(id='sols', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_sale_order_lines',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='number_sale_orders', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sold_items', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='allow_billable', kind=None),
                                    Constant(value='data', kind=None),
                                    Constant(value='number_sols', kind=None),
                                    Constant(value='total_sold', kind=None),
                                    Constant(value='effective_sold', kind=None),
                                    Constant(value='company_unit_name', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='allow_billable',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='sols', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
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
                                    targets=[Name(id='name', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='number_sale_orders', ctx=Load()),
                                            ops=[Gt()],
                                            comparators=[Constant(value=1, kind=None)],
                                        ),
                                        body=ListComp(
                                            elt=Subscript(
                                                value=Name(id='x', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='x', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='sol', ctx=Load()),
                                                            attr='name_get',
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
                                        orelse=Attribute(
                                            value=Name(id='sol', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='sold_items', ctx=Load()),
                                                slice=Constant(value='data', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='color', kind=None),
                                                ],
                                                values=[
                                                    Name(id='name', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='%s / %s %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Name(id='formatLang', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Name(id='qty_delivered', ctx=Load()),
                                                                        Constant(value=1, kind=None),
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
                                                                        Name(id='product_uom_qty', ctx=Load()),
                                                                        Constant(value=1, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                IfExp(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='sol', ctx=Load()),
                                                                            attr='product_uom',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='product_uom_unit', ctx=Load())],
                                                                    ),
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
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    IfExp(
                                                        test=Compare(
                                                            left=Name(id='qty_delivered', ctx=Load()),
                                                            ops=[Gt()],
                                                            comparators=[Name(id='product_uom_qty', ctx=Load())],
                                                        ),
                                                        body=Constant(value='red', kind=None),
                                                        orelse=Constant(value='black', kind=None),
                                                    ),
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
                                            target=Subscript(
                                                value=Name(id='sold_items', ctx=Load()),
                                                slice=Constant(value='total_sold', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='product_uom_qty', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='sold_items', ctx=Load()),
                                                slice=Constant(value='effective_sold', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
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
                                                    Name(id='qty_delivered', ctx=Load()),
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
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remaining', ctx=Store())],
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='sold_items', ctx=Load()),
                                    slice=Constant(value='total_sold', kind=None),
                                    ctx=Load(),
                                ),
                                op=Sub(),
                                right=Subscript(
                                    value=Name(id='sold_items', ctx=Load()),
                                    slice=Constant(value='effective_sold', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='sold_items', ctx=Load()),
                                    slice=Constant(value='remaining', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='value', kind=None),
                                    Constant(value='color', kind=None),
                                ],
                                values=[
                                    Name(id='remaining', ctx=Load()),
                                    IfExp(
                                        test=Compare(
                                            left=Name(id='remaining', ctx=Load()),
                                            ops=[Lt()],
                                            comparators=[Constant(value=0, kind=None)],
                                        ),
                                        body=Constant(value='red', kind=None),
                                        orelse=Constant(value='black', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='sold_items', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_profitability_items',
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
                                    args=[Constant(value='project.group_project_manager', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='data', kind=None)],
                                        values=[List(elts=[], ctx=Load())],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='allow_billable',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='profitability', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_profitability_common',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='margin_color', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='float_is_zero', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='profitability', ctx=Load()),
                                                    slice=Constant(value='margin', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_digits',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='margin_color', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='profitability', ctx=Load()),
                                                                    slice=Constant(value='margin', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            Constant(value='green', kind=None),
                                                        ],
                                                    ),
                                                    Constant(value='red', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Name(id='data', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='value', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Revenues', kind=None)],
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
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='value', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Costs', kind=None)],
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
                                                                slice=Constant(value='costs', kind=None),
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
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='color', kind=None),
                                                    Constant(value='value', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Margin', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(id='margin_color', ctx=Load()),
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
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='action', kind=None),
                                    Constant(value='allow_billable', kind=None),
                                    Constant(value='data', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='allow_billable',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='allow_timesheets',
                                                ctx=Load(),
                                            ),
                                            Constant(value='action_view_timesheet', kind=None),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='allow_billable',
                                        ctx=Load(),
                                    ),
                                    Name(id='data', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_profitability_common',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='costs', kind=None),
                                    Constant(value='margin', kind=None),
                                    Constant(value='revenues', kind=None),
                                ],
                                values=[
                                    Constant(value=0.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profitability', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Constant(value='project_id', kind=None),
                                            Constant(value='amount_untaxed_to_invoice', kind=None),
                                            Constant(value='amount_untaxed_invoiced', kind=None),
                                            Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                            Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                            Constant(value='other_revenues', kind=None),
                                            Constant(value='expense_cost', kind=None),
                                            Constant(value='timesheet_cost', kind=None),
                                            Constant(value='margin', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='project_id', kind=None)],
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
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='profitability', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='profitability', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='profitability', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='costs', kind=None),
                                                    Constant(value='margin', kind=None),
                                                    Constant(value='revenues', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Subscript(
                                                            value=Name(id='profitability', ctx=Load()),
                                                            slice=Constant(value='timesheet_cost', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Name(id='profitability', ctx=Load()),
                                                            slice=Constant(value='expense_cost', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='profitability', ctx=Load()),
                                                        slice=Constant(value='margin', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=Subscript(
                                                                        value=Name(id='profitability', ctx=Load()),
                                                                        slice=Constant(value='amount_untaxed_invoiced', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Subscript(
                                                                        value=Name(id='profitability', ctx=Load()),
                                                                        slice=Constant(value='amount_untaxed_to_invoice', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Name(id='profitability', ctx=Load()),
                                                                    slice=Constant(value='expense_amount_untaxed_invoiced', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Name(id='profitability', ctx=Load()),
                                                                slice=Constant(value='expense_amount_untaxed_to_invoice', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Name(id='profitability', ctx=Load()),
                                                            slice=Constant(value='other_revenues', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                    name='_get_stat_buttons',
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
                            targets=[Name(id='buttons', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Project', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_stat_buttons',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_has_groups',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='hr_timesheet.group_hr_timesheet_approver', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='buttons', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='icon', kind=None),
                                                    Constant(value='text', kind=None),
                                                    Constant(value='number', kind=None),
                                                    Constant(value='action_type', kind=None),
                                                    Constant(value='action', kind=None),
                                                    Constant(value='additional_context', kind=None),
                                                    Constant(value='show', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='clock-o', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Billable Time', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='%s %%', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='billable_percentage',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='object', kind=None),
                                                    Constant(value='action_billable_time_button', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='json', ctx=Load()),
                                                            attr='dumps',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='active_id', kind=None),
                                                                    Constant(value='default_project_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
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
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='allow_timesheets',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='bool', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='analytic_account_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=9, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='buttons', ctx=Load()),
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
            name='ProjectTask',
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
                    value=Constant(value='project.task', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_default_partner_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='project', annotation=None, type_comment=None),
                            arg(arg='parent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_default_partner_id',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='project', ctx=Load()),
                                    Name(id='parent', ctx=Load()),
                                ],
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
                                        operand=Name(id='res', ctx=Load()),
                                    ),
                                    Name(id='project', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='related_project', ctx=Store())],
                                    value=IfExp(
                                        test=UnaryOp(
                                            op=Not(),
                                            operand=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_has_groups',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='!base.group_user,base.group_portal', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        body=Name(id='project', ctx=Load()),
                                        orelse=Call(
                                            func=Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='related_project', ctx=Load()),
                                            attr='pricing_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='employee_rate', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='related_project', ctx=Load()),
                                                            attr='sale_line_employee_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='sale_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='order_partner_id',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=1, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sale_order_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Constant(value="['|', '|', ('partner_id', '=', partner_id), ('partner_id', 'child_of', commercial_partner_id), ('partner_id', 'parent_of', partner_id)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='so_analytic_account_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='sale_order_id.analytic_account_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Sale Order Analytic Account', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pricing_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='project_id.pricing_type', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_project_map_empty', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is Project map empty', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_is_project_map_empty', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='has_multi_sol', ctx=Store())],
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
                                value=Constant(value='_compute_has_multi_sol', kind=None),
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
                    targets=[Name(id='allow_billable', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='project_id.allow_billable', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='timesheet_product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='project_id.timesheet_product_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='remaining_hours_so', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Remaining Hours on SO', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_remaining_hours_so', kind=None),
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
                    targets=[Name(id='remaining_hours_available', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='sale_line_id.remaining_hours_available', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='SELF_READABLE_FIELDS',
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
                            value=BinOp(
                                left=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='SELF_READABLE_FIELDS',
                                    ctx=Load(),
                                ),
                                op=BitOr(),
                                right=Set(
                                    elts=[
                                        Constant(value='allow_billable', kind=None),
                                        Constant(value='remaining_hours_available', kind=None),
                                        Constant(value='remaining_hours_so', kind=None),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_remaining_hours_so',
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
                            targets=[Name(id='timesheets', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='timesheet_ids',
                                        ctx=Load(),
                                    ),
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
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='t', ctx=Load()),
                                                            attr='task_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='sale_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='t', ctx=Load()),
                                                                    attr='so_line',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='t', ctx=Load()),
                                                                        attr='_origin',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='so_line',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='so_line',
                                                        ctx=Load(),
                                                    ),
                                                    attr='remaining_hours_available',
                                                    ctx=Load(),
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
                            targets=[Name(id='mapped_remaining_hours', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='_origin',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=BoolOp(
                                    op=Or(),
                                    values=[
                                        BoolOp(
                                            op=And(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='task', ctx=Load()),
                                                    attr='sale_line_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task', ctx=Load()),
                                                        attr='sale_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='remaining_hours',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        Constant(value=0.0, kind=None),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='task', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
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
                        For(
                            target=Name(id='timesheet', ctx=Store()),
                            iter=Name(id='timesheets', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='delta', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='timesheet', ctx=Load()),
                                                attr='_origin',
                                                ctx=Load(),
                                            ),
                                            attr='so_line',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='timesheet', ctx=Load()),
                                                    attr='task_id',
                                                    ctx=Load(),
                                                ),
                                                attr='sale_line_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='delta', ctx=Store()),
                                            op=Add(),
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='timesheet', ctx=Load()),
                                                    attr='_origin',
                                                    ctx=Load(),
                                                ),
                                                attr='unit_amount',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='timesheet', ctx=Load()),
                                            attr='so_line',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='timesheet', ctx=Load()),
                                                    attr='task_id',
                                                    ctx=Load(),
                                                ),
                                                attr='sale_line_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='delta', ctx=Store()),
                                            op=Sub(),
                                            value=Attribute(
                                                value=Name(id='timesheet', ctx=Load()),
                                                attr='unit_amount',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='delta', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='mapped_remaining_hours', ctx=Load()),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='timesheet', ctx=Load()),
                                                            attr='task_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_origin',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='timesheet', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='delta', ctx=Load()),
                                                    Name(id='uom_hour', ctx=Load()),
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
                        For(
                            target=Name(id='task', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task', ctx=Load()),
                                            attr='remaining_hours_so',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='mapped_remaining_hours', ctx=Load()),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='_origin',
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
                                Constant(value='sale_line_id', kind=None),
                                Constant(value='timesheet_ids', kind=None),
                                Constant(value='timesheet_ids.unit_amount', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_analytic_account_active',
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
                                    attr='_compute_analytic_account_active',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='task', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task', ctx=Load()),
                                            attr='analytic_account_active',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='analytic_account_active',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task', ctx=Load()),
                                                    attr='so_analytic_account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='active',
                                                ctx=Load(),
                                            ),
                                        ],
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
                            args=[Constant(value='so_analytic_account_id.active', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_sale_order_id',
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
                            targets=[Name(id='billable_tasks', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='allow_billable', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProjectTask', ctx=Load()),
                                            Name(id='billable_tasks', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_sale_order_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=BinOp(
                                        left=Name(id='self', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='billable_tasks', ctx=Load()),
                                    ),
                                    attr='sale_order_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
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
                            args=[Constant(value='allow_billable', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_sale_line',
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
                            targets=[Name(id='billable_tasks', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='allow_billable', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Name(id='self', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='billable_tasks', ctx=Load()),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='sale_line_id', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProjectTask', ctx=Load()),
                                            Name(id='billable_tasks', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_sale_line',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='task', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='billable_tasks', ctx=Load()),
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
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='sale_line_id',
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
                                            value=Name(id='task', ctx=Load()),
                                            attr='sale_line_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task', ctx=Load()),
                                            attr='_get_last_sol_of_customer',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                Constant(value='commercial_partner_id', kind=None),
                                Constant(value='sale_line_id.order_partner_id.commercial_partner_id', kind=None),
                                Constant(value='parent_id.sale_line_id', kind=None),
                                Constant(value='project_id.sale_line_id', kind=None),
                                Constant(value='allow_billable', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_is_project_map_empty',
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
                            target=Name(id='task', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task', ctx=Load()),
                                            attr='is_project_map_empty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='bool', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='task', ctx=Load()),
                                                                attr='sudo',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='project_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sale_line_employee_ids',
                                                    ctx=Load(),
                                                ),
                                            ],
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
                            args=[Constant(value='project_id.sale_line_employee_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_has_multi_sol',
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
                            target=Name(id='task', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='task', ctx=Load()),
                                            attr='has_multi_sol',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='timesheet_ids',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='task', ctx=Load()),
                                                        attr='timesheet_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='so_line',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='task', ctx=Load()),
                                                        attr='sale_line_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                            args=[Constant(value='timesheet_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_last_sol_of_customer',
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='commercial_partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='allow_billable',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value='=', kind=None),
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
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='is_service', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='order_partner_id', kind=None),
                                            Constant(value='child_of', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='commercial_partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='is_expense', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='in', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='sale', kind=None),
                                                    Constant(value='done', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='remaining_hours', kind=None),
                                            Constant(value='>', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='project_id',
                                                ctx=Load(),
                                            ),
                                            attr='pricing_type',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='task_rate', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_sale_order_id',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='commercial_partner_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='project_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='commercial_partner_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='order_id', kind=None),
                                                    Constant(value='=?', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='project_sale_order_id',
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
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
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
                    name='_get_timesheet',
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
                            targets=[Name(id='timesheet_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProjectTask', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_timesheet',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='timesheet_ids', ctx=Load()),
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
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='_is_not_billed',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
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
                    name='_get_action_view_so_ids',
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
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='sale_order_id',
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='timesheet_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='so_line',
                                                            ctx=Load(),
                                                        ),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ProjectTaskRecurrence',
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
                    value=Constant(value='project.task.recurrence', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_recurring_fields',
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
                            value=BinOp(
                                left=List(
                                    elts=[Constant(value='so_analytic_account_id', kind=None)],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[
                                                Name(id='ProjectTaskRecurrence', ctx=Load()),
                                                Name(id='self', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='_get_recurring_fields',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
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
