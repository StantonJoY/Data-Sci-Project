Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='operator',
            names=[alias(name='itemgetter', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='date_utils', asname=None),
                alias(name='groupby', asname='groupbyelem'),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[
                alias(name='AND', asname=None),
                alias(name='OR', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers.portal',
            names=[
                alias(name='CustomerPortal', asname=None),
                alias(name='pager', asname='portal_pager'),
            ],
            level=0,
        ),
        ClassDef(
            name='TimesheetCustomerPortal',
            bases=[Name(id='CustomerPortal', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_prepare_home_portal_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='counters', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_prepare_home_portal_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='counters', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='timesheet_count', kind=None),
                                ops=[In()],
                                comparators=[Name(id='counters', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='Timesheet', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Timesheet', ctx=Load()),
                                            attr='_timesheet_get_portal_domain',
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
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='timesheet_count', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Timesheet', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                    name='_get_searchbar_inputs',
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
                                    Constant(value='all', kind=None),
                                    Constant(value='employee', kind=None),
                                    Constant(value='project', kind=None),
                                    Constant(value='task', kind=None),
                                    Constant(value='name', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='all', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Search in All', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='employee', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Search in Employee', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='project', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Search in Project', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='task', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Search in Task', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='name', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Search in Description', kind=None)],
                                                keywords=[],
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
                    name='_task_get_searchbar_sortings',
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_task_get_searchbar_sortings',
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
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='progress', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='label', kind=None),
                                    Constant(value='order', kind=None),
                                    Constant(value='sequence', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Progress', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='progress asc', kind=None),
                                    Constant(value=9, kind=None),
                                ],
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
                FunctionDef(
                    name='_get_searchbar_groupby',
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
                                    Constant(value='none', kind=None),
                                    Constant(value='project', kind=None),
                                    Constant(value='task', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='employee', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='none', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='None', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='project', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Project', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='task', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Task', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='date', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Date', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='input', kind=None),
                                            Constant(value='label', kind=None),
                                        ],
                                        values=[
                                            Constant(value='employee', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Employee', kind=None)],
                                                keywords=[],
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
                    name='_get_search_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_in', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='search_domain', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='search_in', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='project', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='search_domain', ctx=Store())],
                                    value=Call(
                                        func=Name(id='OR', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='project_id', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    Name(id='search', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='search_in', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='search_domain', ctx=Store())],
                                    value=Call(
                                        func=Name(id='OR', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    Name(id='search', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='search_in', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='employee', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='search_domain', ctx=Store())],
                                    value=Call(
                                        func=Name(id='OR', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='employee_id', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    Name(id='search', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='search_in', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='task', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='search_domain', ctx=Store())],
                                    value=Call(
                                        func=Name(id='OR', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='task_id', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    Name(id='search', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='search_domain', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_groupby_mapping',
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
                                    Constant(value='project', kind=None),
                                    Constant(value='task', kind=None),
                                    Constant(value='employee', kind=None),
                                    Constant(value='date', kind=None),
                                ],
                                values=[
                                    Constant(value='project_id', kind=None),
                                    Constant(value='task_id', kind=None),
                                    Constant(value='employee_id', kind=None),
                                    Constant(value='date', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_searchbar_sortings',
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
                                    Constant(value='date', kind=None),
                                    Constant(value='employee', kind=None),
                                    Constant(value='project', kind=None),
                                    Constant(value='task', kind=None),
                                    Constant(value='name', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='order', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Newest', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='date desc', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='order', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Employee', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='order', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Project', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='project_id', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='order', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Task', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='task_id', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='order', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Description', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='name', kind=None),
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
                    name='portal_my_timesheets',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='sortby', annotation=None, type_comment=None),
                            arg(arg='filterby', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                            arg(arg='search_in', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=1, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='all', kind=None),
                            Constant(value='none', kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Timesheet', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.analytic.line', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Timesheet', ctx=Load()),
                                    attr='_timesheet_get_portal_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Timesheet_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Timesheet', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_portal_layout_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='_items_per_page', ctx=Store())],
                            value=Constant(value=100, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='searchbar_sortings', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_searchbar_sortings',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='searchbar_inputs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_searchbar_inputs',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='searchbar_groupby', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_searchbar_groupby',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='today', ctx=Store())],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='quarter_start', ctx=Store()),
                                        Name(id='quarter_end', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='date_utils', ctx=Load()),
                                    attr='get_quarter',
                                    ctx=Load(),
                                ),
                                args=[Name(id='today', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_week', ctx=Store())],
                            value=BinOp(
                                left=Name(id='today', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='relativedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='weeks',
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_month', ctx=Store())],
                            value=BinOp(
                                left=Name(id='today', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='relativedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='months',
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_year', ctx=Store())],
                            value=BinOp(
                                left=Name(id='today', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='relativedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='years',
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='searchbar_filters', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='all', kind=None),
                                    Constant(value='today', kind=None),
                                    Constant(value='week', kind=None),
                                    Constant(value='month', kind=None),
                                    Constant(value='year', kind=None),
                                    Constant(value='quarter', kind=None),
                                    Constant(value='last_week', kind=None),
                                    Constant(value='last_month', kind=None),
                                    Constant(value='last_year', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='All', kind=None)],
                                                keywords=[],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Today', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='today', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This week', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='start_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='today', ctx=Load()),
                                                                    Constant(value='week', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='end_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='today', ctx=Load()),
                                                                    Constant(value='week', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This month', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='start_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='today', ctx=Load()),
                                                                    Constant(value='month', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='end_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='today', ctx=Load()),
                                                                    Constant(value='month', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This year', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='start_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='today', ctx=Load()),
                                                                    Constant(value='year', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='end_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='today', ctx=Load()),
                                                                    Constant(value='year', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This Quarter', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Name(id='quarter_start', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<=', kind=None),
                                                            Name(id='quarter_end', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Last week', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='start_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='last_week', ctx=Load()),
                                                                    Constant(value='week', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='end_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='last_week', ctx=Load()),
                                                                    Constant(value='week', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Last month', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='start_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='last_month', ctx=Load()),
                                                                    Constant(value='month', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='end_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='last_month', ctx=Load()),
                                                                    Constant(value='month', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Last year', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='start_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='last_year', ctx=Load()),
                                                                    Constant(value='year', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='date_utils', ctx=Load()),
                                                                    attr='end_of',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='last_year', ctx=Load()),
                                                                    Constant(value='year', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='sortby', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sortby', ctx=Store())],
                                    value=Constant(value='date', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='order', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='searchbar_sortings', ctx=Load()),
                                    slice=Name(id='sortby', ctx=Load()),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='order', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='filterby', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filterby', ctx=Store())],
                                    value=Constant(value='all', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Name(id='AND', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='domain', ctx=Load()),
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='searchbar_filters', ctx=Load()),
                                                    slice=Name(id='filterby', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='domain', kind=None),
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='search', ctx=Load()),
                                    Name(id='search_in', ctx=Load()),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_search_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='search_in', ctx=Load()),
                                            Name(id='search', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='timesheet_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Timesheet_sudo', ctx=Load()),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pager', ctx=Store())],
                            value=Call(
                                func=Name(id='portal_pager', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=Constant(value='/my/timesheets', kind=None),
                                    ),
                                    keyword(
                                        arg='url_args',
                                        value=Dict(
                                            keys=[
                                                Constant(value='sortby', kind=None),
                                                Constant(value='search_in', kind=None),
                                                Constant(value='search', kind=None),
                                                Constant(value='filterby', kind=None),
                                                Constant(value='groupby', kind=None),
                                            ],
                                            values=[
                                                Name(id='sortby', ctx=Load()),
                                                Name(id='search_in', ctx=Load()),
                                                Name(id='search', ctx=Load()),
                                                Name(id='filterby', ctx=Load()),
                                                Name(id='groupby', ctx=Load()),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='total',
                                        value=Name(id='timesheet_count', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='page',
                                        value=Name(id='page', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='step',
                                        value=Name(id='_items_per_page', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_timesheets',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Assign(
                                    targets=[Name(id='groupby_mapping', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_groupby_mapping',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='field', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='groupby_mapping', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='groupby', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='orderby', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='field', ctx=Load()),
                                        body=BinOp(
                                            left=Constant(value='%s, %s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Name(id='field', ctx=Load()),
                                                    Name(id='order', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        orelse=Name(id='order', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='timesheets', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Timesheet_sudo', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='order',
                                                value=Name(id='orderby', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='limit',
                                                value=Name(id='_items_per_page', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='offset',
                                                value=Subscript(
                                                    value=Name(id='pager', ctx=Load()),
                                                    slice=Constant(value='offset', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='field', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='groupby', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='date', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='time_data', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Timesheet_sudo', ctx=Load()),
                                                            attr='read_group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='domain', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value='unit_amount:sum', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[Constant(value='date:day', kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='mapped_time', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[
                                                            ListComp(
                                                                elt=Tuple(
                                                                    elts=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='datetime', ctx=Load()),
                                                                                        attr='strptime',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Subscript(
                                                                                            value=Name(id='m', ctx=Load()),
                                                                                            slice=Constant(value='date:day', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        Constant(value='%d %b %Y', kind=None),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='date',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        Subscript(
                                                                            value=Name(id='m', ctx=Load()),
                                                                            slice=Constant(value='unit_amount', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='m', ctx=Store()),
                                                                        iter=Name(id='time_data', ctx=Load()),
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
                                                Assign(
                                                    targets=[Name(id='grouped_timesheets', ctx=Store())],
                                                    value=ListComp(
                                                        elt=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='Timesheet_sudo', ctx=Load()),
                                                                        attr='concat',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Starred(
                                                                            value=Name(id='g', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='mapped_time', ctx=Load()),
                                                                    slice=Name(id='k', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Tuple(
                                                                    elts=[
                                                                        Name(id='k', ctx=Store()),
                                                                        Name(id='g', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                                iter=Call(
                                                                    func=Name(id='groupbyelem', ctx=Load()),
                                                                    args=[
                                                                        Name(id='timesheets', ctx=Load()),
                                                                        Call(
                                                                            func=Name(id='itemgetter', ctx=Load()),
                                                                            args=[Constant(value='date', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Name(id='time_data', ctx=Store()),
                                                        Name(id='time_data', ctx=Store()),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Timesheet_sudo', ctx=Load()),
                                                            attr='read_group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='domain', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Name(id='field', ctx=Load()),
                                                                    Constant(value='unit_amount:sum', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[Name(id='field', ctx=Load())],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='mapped_time', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[
                                                            ListComp(
                                                                elt=Tuple(
                                                                    elts=[
                                                                        IfExp(
                                                                            test=Subscript(
                                                                                value=Name(id='m', ctx=Load()),
                                                                                slice=Name(id='field', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            body=Subscript(
                                                                                value=Subscript(
                                                                                    value=Name(id='m', ctx=Load()),
                                                                                    slice=Name(id='field', ctx=Load()),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            orelse=Constant(value=False, kind=None),
                                                                        ),
                                                                        Subscript(
                                                                            value=Name(id='m', ctx=Load()),
                                                                            slice=Constant(value='unit_amount', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='m', ctx=Store()),
                                                                        iter=Name(id='time_data', ctx=Load()),
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
                                                Assign(
                                                    targets=[Name(id='grouped_timesheets', ctx=Store())],
                                                    value=ListComp(
                                                        elt=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='Timesheet_sudo', ctx=Load()),
                                                                        attr='concat',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Starred(
                                                                            value=Name(id='g', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='mapped_time', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='k', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Tuple(
                                                                    elts=[
                                                                        Name(id='k', ctx=Store()),
                                                                        Name(id='g', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                                iter=Call(
                                                                    func=Name(id='groupbyelem', ctx=Load()),
                                                                    args=[
                                                                        Name(id='timesheets', ctx=Load()),
                                                                        Call(
                                                                            func=Name(id='itemgetter', ctx=Load()),
                                                                            args=[Name(id='field', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Name(id='timesheets', ctx=Load()),
                                                    Name(id='grouped_timesheets', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='grouped_timesheets', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='timesheets', ctx=Load()),
                                        body=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='timesheets', ctx=Load()),
                                                        Call(
                                                            func=Name(id='sum', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='Timesheet_sudo', ctx=Load()),
                                                                                attr='search',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='domain', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='mapped',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='unit_amount', kind=None)],
                                                                    keywords=[],
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
                                        orelse=List(elts=[], ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='timesheets', ctx=Load()),
                                            Name(id='grouped_timesheets', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='timesheets', ctx=Store()),
                                        Name(id='grouped_timesheets', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='get_timesheets', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='timesheets', kind=None),
                                            Constant(value='grouped_timesheets', kind=None),
                                            Constant(value='page_name', kind=None),
                                            Constant(value='default_url', kind=None),
                                            Constant(value='pager', kind=None),
                                            Constant(value='searchbar_sortings', kind=None),
                                            Constant(value='search_in', kind=None),
                                            Constant(value='search', kind=None),
                                            Constant(value='sortby', kind=None),
                                            Constant(value='groupby', kind=None),
                                            Constant(value='searchbar_inputs', kind=None),
                                            Constant(value='searchbar_groupby', kind=None),
                                            Constant(value='searchbar_filters', kind=None),
                                            Constant(value='filterby', kind=None),
                                            Constant(value='is_uom_day', kind=None),
                                        ],
                                        values=[
                                            Name(id='timesheets', ctx=Load()),
                                            Name(id='grouped_timesheets', ctx=Load()),
                                            Constant(value='timesheet', kind=None),
                                            Constant(value='/my/timesheets', kind=None),
                                            Name(id='pager', ctx=Load()),
                                            Name(id='searchbar_sortings', ctx=Load()),
                                            Name(id='search_in', ctx=Load()),
                                            Name(id='search', ctx=Load()),
                                            Name(id='sortby', ctx=Load()),
                                            Name(id='groupby', ctx=Load()),
                                            Name(id='searchbar_inputs', ctx=Load()),
                                            Name(id='searchbar_groupby', ctx=Load()),
                                            Call(
                                                func=Name(id='OrderedDict', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='sorted', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='searchbar_filters', ctx=Load()),
                                                                    attr='items',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='filterby', ctx=Load()),
                                            Call(
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='hr_timesheet.portal_my_timesheets', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/my/timesheets', kind=None),
                                        Constant(value='/my/timesheets/page/<int:page>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
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
