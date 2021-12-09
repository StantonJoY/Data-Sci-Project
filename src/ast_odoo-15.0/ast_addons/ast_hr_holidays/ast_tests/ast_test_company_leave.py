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
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestCompanyLeave',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Test leaves for a whole company, conflict resolutions ', kind=None),
                ),
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
                                            Name(id='TestCompanyLeave', ctx=Load()),
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
                                    attr='bank_holiday',
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
                                            Constant(value='responsible_id', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='requires_allocation', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bank Holiday', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
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
                                    attr='employee',
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
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='company_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='My Employee', kind=None),
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_leave_whole_company_01',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Hol11', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
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
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=3, kind=None),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='_compute_date_from_to',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='company_leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='holiday_type', kind=None),
                                            Constant(value='mode_company_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bank Holiday', kind=None),
                                            Constant(value='company', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_holiday',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='company_leave', ctx=Load()),
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
                                    value=Name(id='company_leave', ctx=Load()),
                                    attr='action_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='all_leaves', ctx=Store())],
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
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='employee',
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id', kind=None),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='all_leaves', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
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
                                        value=Name(id='leave', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='refuse', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='confirm', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='confirm', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='validate', kind=None),
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
                    name='test_leave_whole_company_02',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paid_time_off',
                                        ctx=Load(),
                                    ),
                                    attr='request_unit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='half_day', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Hol11', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
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
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=3, kind=None),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='_compute_date_from_to',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='company_leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='holiday_type', kind=None),
                                            Constant(value='mode_company_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bank Holiday', kind=None),
                                            Constant(value='company', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_holiday',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='company_leave', ctx=Load()),
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
                                    value=Name(id='company_leave', ctx=Load()),
                                    attr='action_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='all_leaves', ctx=Store())],
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
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='employee',
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id', kind=None),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='all_leaves', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
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
                                        value=Name(id='leave', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='refuse', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='confirm', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='confirm', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='validate', kind=None),
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
                    name='test_leave_whole_company_03',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paid_time_off',
                                        ctx=Load(),
                                    ),
                                    attr='request_unit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='half_day', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                            Constant(value='request_unit_half', kind=None),
                                            Constant(value='request_date_from_period', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Hol11', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
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
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=0.5, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='am', kind=None),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='_compute_date_from_to',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='company_leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='holiday_type', kind=None),
                                            Constant(value='mode_company_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bank Holiday', kind=None),
                                            Constant(value='company', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_holiday',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='company_leave', ctx=Load()),
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
                                    value=Name(id='company_leave', ctx=Load()),
                                    attr='action_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='all_leaves', ctx=Store())],
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
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='employee',
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id', kind=None),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='all_leaves', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
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
                                        value=Name(id='leave', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='refuse', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='validate', kind=None),
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
                    name='test_leave_whole_company_04',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paid_time_off',
                                        ctx=Load(),
                                    ),
                                    attr='request_unit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='day', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Hol11', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
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
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='_compute_date_from_to',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='company_leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='holiday_type', kind=None),
                                            Constant(value='mode_company_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bank Holiday', kind=None),
                                            Constant(value='company', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_holiday',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='company_leave', ctx=Load()),
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
                                    value=Name(id='company_leave', ctx=Load()),
                                    attr='action_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='all_leaves', ctx=Store())],
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
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='employee',
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id', kind=None),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='all_leaves', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
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
                                        value=Name(id='leave', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='refuse', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='validate', kind=None),
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
                    name='test_leave_whole_company_06',
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='employee',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='attendance_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Monday Morning', kind=None),
                                                                    Constant(value='0', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value='morning', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Monday Afternoon', kind=None),
                                                                    Constant(value='0', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=17, kind=None),
                                                                    Constant(value='afternoon', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Wednesday Morning', kind=None),
                                                                    Constant(value='2', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value='morning', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Wednesday Afternoon', kind=None),
                                                                    Constant(value='2', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=17, kind=None),
                                                                    Constant(value='afternoon', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Friday Morning', kind=None),
                                                                    Constant(value='4', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value='morning', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Friday Afternoon', kind=None),
                                                                    Constant(value='4', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=17, kind=None),
                                                                    Constant(value='afternoon', kind=None),
                                                                ],
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
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Hol11', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
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
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=3, kind=None),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='_compute_date_from_to',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='company_leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='holiday_type', kind=None),
                                            Constant(value='mode_company_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bank Holiday', kind=None),
                                            Constant(value='company', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_holiday',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='company_leave', ctx=Load()),
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
                                    value=Name(id='company_leave', ctx=Load()),
                                    attr='action_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='all_leaves', ctx=Store())],
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
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='employee',
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id', kind=None),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='all_leaves', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
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
                                        value=Name(id='leave', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='refuse', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='confirm', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='number_of_days',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='all_leaves', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='validate', kind=None),
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
                    name='test_leave_whole_company_07',
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
                                                        value=Name(id='self', ctx=Load()),
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
                            targets=[Name(id='leaves', ctx=Store())],
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
                                                        value=Name(id='self', ctx=Load()),
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
                                                        Constant(value=3, kind=None),
                                                        Constant(value=29, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='date', ctx=Load()),
                                                    args=[
                                                        Constant(value=2020, kind=None),
                                                        Constant(value=4, kind=None),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Constant(value=3, kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='employee', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='employees', ctx=Load()),
                                                    slice=Slice(
                                                        lower=Constant(value=0, kind=None),
                                                        upper=Constant(value=15, kind=None),
                                                        step=None,
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leaves', ctx=Load()),
                                    attr='_compute_date_from_to',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='company_leave', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='holiday_type', kind=None),
                                            Constant(value='mode_company_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='request_date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='request_date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bank Holiday', kind=None),
                                            Constant(value='company', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_holiday',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='company_leave', ctx=Load()),
                                    attr='_compute_date_from_to',
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
                                                value=Constant(value=772, kind=None),
                                            ),
                                            keyword(
                                                arg='admin',
                                                value=Constant(value=865, kind=None),
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
                                            value=Name(id='company_leave', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
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
                                                    Constant(value='holiday_status_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='bank_holiday',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='leaves', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=102, kind=None),
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
                    args=[Constant(value='company_leave', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
