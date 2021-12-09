Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[
                alias(name='date', asname=None),
                alias(name='datetime', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hr_work_entry_holidays.tests.common',
            names=[alias(name='TestWorkEntryHolidaysBase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='users', asname=None),
                alias(name='warmup', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestWorkEntryHolidaysPerformance',
            bases=[Name(id='TestWorkEntryHolidaysBase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                        args=[
                                            Name(id='TestWorkEntryHolidaysPerformance', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='jack',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Jack', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='employees',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='richard_emp',
                                    ctx=Load(),
                                ),
                                op=BitOr(),
                                right=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='jack',
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
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.contract', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='date_start', kind=None),
                                                Constant(value='date_end', kind=None),
                                                Constant(value='name', kind=None),
                                                Constant(value='wage', kind=None),
                                                Constant(value='state', kind=None),
                                                Constant(value='employee_id', kind=None),
                                                Constant(value='date_generated_from', kind=None),
                                                Constant(value='date_generated_to', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Name(id='date', ctx=Load()),
                                                    args=[
                                                        Constant(value=2018, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='date', ctx=Load()),
                                                    args=[
                                                        Constant(value=2018, kind=None),
                                                        Constant(value=2, kind=None),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                BinOp(
                                                    left=Constant(value='Contract for %s', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='employee', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Constant(value=5000.0, kind=None),
                                                Constant(value='open', kind=None),
                                                Attribute(
                                                    value=Name(id='employee', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Name(id='datetime', ctx=Load()),
                                                    args=[
                                                        Constant(value=2018, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='datetime', ctx=Load()),
                                                    args=[
                                                        Constant(value=2018, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='employee', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='employees',
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
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_performance_leave_validate',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='richard_emp',
                                        ctx=Load(),
                                    ),
                                    attr='generate_work_entries',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=18, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=92, kind=None),
                                            ),
                                            keyword(
                                                arg='admin',
                                                value=Constant(value=93, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='leave', ctx=Load()),
                                            attr='action_validate',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='action_refuse',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='admin', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_performance_leave_write',
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
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=18, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=19, kind=None),
                                            ),
                                            keyword(
                                                arg='admin',
                                                value=Constant(value=19, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='leave', ctx=Load()),
                                            attr='date_to',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=19, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='action_refuse',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='admin', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_performance_leave_create',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=25, kind=None),
                                            ),
                                            keyword(
                                                arg='admin',
                                                value=Constant(value=26, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='leave', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_leave',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=18, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='action_refuse',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='admin', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_performance_leave_confirm',
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
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=18, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='action_draft',
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=18, kind=None),
                                            ),
                                            keyword(
                                                arg='admin',
                                                value=Constant(value=19, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='leave', ctx=Load()),
                                            attr='action_confirm',
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
                            targets=[
                                Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='refuse', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='admin', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestWorkEntryHolidaysPerformancesBigData',
            bases=[Name(id='TestWorkEntryHolidaysBase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                        args=[
                                            Name(id='TestWorkEntryHolidaysPerformancesBigData', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='A company', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='paid_time_off',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.leave.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='request_unit', kind=None),
                                            Constant(value='leave_validation_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='requires_allocation', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Paid Time Off', kind=None),
                                            Constant(value='day', kind=None),
                                            Constant(value='both', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='no', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='employees',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='company_id', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=Constant(value='Employee %s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='i', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[Constant(value=100, kind=None)],
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='contracts',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.contract', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='date_start', kind=None),
                                                Constant(value='date_end', kind=None),
                                                Constant(value='name', kind=None),
                                                Constant(value='wage', kind=None),
                                                Constant(value='state', kind=None),
                                                Constant(value='employee_id', kind=None),
                                                Constant(value='date_generated_from', kind=None),
                                                Constant(value='date_generated_to', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Name(id='date', ctx=Load()),
                                                    args=[
                                                        Constant(value=2018, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Constant(value=False, kind=None),
                                                BinOp(
                                                    left=Constant(value='Contract for %s', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='employee', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Constant(value=5000.0, kind=None),
                                                Constant(value='open', kind=None),
                                                Attribute(
                                                    value=Name(id='employee', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Name(id='datetime', ctx=Load()),
                                                    args=[
                                                        Constant(value=2018, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='datetime', ctx=Load()),
                                                    args=[
                                                        Constant(value=2018, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='employee', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='employees',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='leaves',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.leave', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='employee_id', kind=None),
                                                Constant(value='holiday_status_id', kind=None),
                                                Constant(value='request_date_from', kind=None),
                                                Constant(value='request_date_to', kind=None),
                                                Constant(value='number_of_days', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=Constant(value='Holiday - %s', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='employee', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Attribute(
                                                    value=Name(id='employee', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='paid_time_off',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Name(id='date', ctx=Load()),
                                                    args=[
                                                        Constant(value=2020, kind=None),
                                                        Constant(value=8, kind=None),
                                                        Constant(value=3, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='date', ctx=Load()),
                                                    args=[
                                                        Constant(value=2020, kind=None),
                                                        Constant(value=8, kind=None),
                                                        Constant(value=7, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Constant(value=5, kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='employee', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='employees',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='leaves',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_date_from_to',
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
                                        value=Name(id='cls', ctx=Load()),
                                        attr='leaves',
                                        ctx=Load(),
                                    ),
                                    attr='action_approve',
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
                                        value=Name(id='cls', ctx=Load()),
                                        attr='leaves',
                                        ctx=Load(),
                                    ),
                                    attr='action_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_work_entries_generation_perf',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=11319, kind=None),
                                            ),
                                            keyword(
                                                arg='admin',
                                                value=Constant(value=11522, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='work_entries', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='contracts',
                                                ctx=Load(),
                                            ),
                                            attr='_generate_work_entries',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=7, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=31, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='work_entries', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=8800, kind=None),
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
                    args=[Constant(value='work_entry_perf', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
