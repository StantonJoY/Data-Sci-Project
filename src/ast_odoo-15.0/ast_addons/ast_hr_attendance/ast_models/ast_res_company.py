Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[alias(name='OR', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ResCompany',
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
                    value=Constant(value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='hr_attendance_overtime', ctx=Store())],
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
                                value=Constant(value='Count Extra Hours', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='overtime_start_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Extra Hours Starting Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='overtime_company_threshold', ctx=Store())],
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
                                value=Constant(value='Tolerance Time In Favor Of Company', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='overtime_employee_threshold', ctx=Store())],
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
                                value=Constant(value='Tolerance Time In Favor Of Employee', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
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
                        Assign(
                            targets=[Name(id='search_domain', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='delete_domain', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='overtime_enabled_companies', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='hr_attendance_overtime', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_disabling_overtime', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='hr_attendance_overtime', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='hr_attendance_overtime', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Name(id='overtime_enabled_companies', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='delete_domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='overtime_enabled_companies', ctx=Load()),
                                                        attr='ids',
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
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='overtime_start_date', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='is_disabling_overtime', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='start_date', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='hr_attendance_overtime', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='overtime_start_date', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='is_disabling_overtime', ctx=Load()),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='start_date', ctx=Load()),
                                            Compare(
                                                left=Constant(value='overtime_company_threshold', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='overtime_employee_threshold', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='company', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='start_date', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='company', ctx=Load()),
                                                                        attr='overtime_start_date',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='vals', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='overtime_company_threshold', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='company', ctx=Load()),
                                                                        attr='overtime_company_threshold',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='vals', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='overtime_employee_threshold', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='company', ctx=Load()),
                                                                attr='overtime_employee_threshold',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                                                                                    Constant(value='employee_id.company_id', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='company', ctx=Load()),
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
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='company', ctx=Load()),
                                                                    attr='overtime_start_date',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Name(id='start_date', ctx=Load()),
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
                                                                                            Constant(value='employee_id.company_id', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Name(id='company', ctx=Load()),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='check_in', kind=None),
                                                                                            Constant(value='>=', kind=None),
                                                                                            Name(id='start_date', ctx=Load()),
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
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='start_date', ctx=Load()),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='company', ctx=Load()),
                                                                            attr='overtime_start_date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Gt()],
                                                                        comparators=[Name(id='start_date', ctx=Load())],
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
                                                                                                    Constant(value='employee_id.company_id', kind=None),
                                                                                                    Constant(value='=', kind=None),
                                                                                                    Attribute(
                                                                                                        value=Name(id='company', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Constant(value='check_in', kind=None),
                                                                                                    Constant(value='>=', kind=None),
                                                                                                    Name(id='start_date', ctx=Load()),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Constant(value='check_in', kind=None),
                                                                                                    Constant(value='<=', kind=None),
                                                                                                    Attribute(
                                                                                                        value=Name(id='company', ctx=Load()),
                                                                                                        attr='overtime_start_date',
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
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='start_date', ctx=Load()),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='company', ctx=Load()),
                                                                                    attr='overtime_start_date',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Lt()],
                                                                                comparators=[Name(id='start_date', ctx=Load())],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='delete_domain', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='OR', ctx=Load()),
                                                                                args=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Name(id='delete_domain', ctx=Load()),
                                                                                            List(
                                                                                                elts=[
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='company_id', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Attribute(
                                                                                                                value=Name(id='company', ctx=Load()),
                                                                                                                attr='id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='date', kind=None),
                                                                                                            Constant(value='<', kind=None),
                                                                                                            Name(id='start_date', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='delete_domain', ctx=Load()),
                            body=[
                                Expr(
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
                                                        slice=Constant(value='hr.attendance.overtime', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='delete_domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='search_domain', ctx=Load()),
                            body=[
                                Expr(
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
                                                        slice=Constant(value='hr.attendance', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='search_domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='_update_overtime',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
