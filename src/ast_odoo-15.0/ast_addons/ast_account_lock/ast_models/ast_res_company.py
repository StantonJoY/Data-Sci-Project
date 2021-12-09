Module(
    body=[
        Import(
            names=[alias(name='calendar', asname=None)],
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
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
                FunctionDef(
                    name='_autorise_lock_date_changes',
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
                            value=Constant(value="Check the lock dates for the current companies. This can't be done in a api.constrains because we need\n        to perform some comparison between new/old values. This method forces the lock dates to be irreversible.\n        * You cannot set stricter restrictions on advisors than on users.\n        Therefore, the All Users Lock Date must be anterior (or equal) to the Invoice/Bills Lock Date.\n        * You cannot lock a period that has not yet ended.\n        Therefore, the All Users Lock Date must be anterior (or equal) to the last day of the previous month.\n        * Any new All Users Lock Date must be posterior (or equal) to the previous one.\n        * You cannot delete a tax lock date, lock a period that is not finished yet or the tax lock date must be set after\n        the last day of the previous month.\n        :param vals: The values passed to the write method.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='period_lock_date', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='period_lock_date', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='period_lock_date', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fiscalyear_lock_date', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='fiscalyear_lock_date', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='fiscalyear_lock_date', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_lock_date', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='tax_lock_date', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='tax_lock_date', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='previous_month', ctx=Store())],
                            value=BinOp(
                                left=Call(
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
                            targets=[Name(id='days_previous_month', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='calendar', ctx=Load()),
                                    attr='monthrange',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='previous_month', ctx=Load()),
                                        attr='year',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='previous_month', ctx=Load()),
                                        attr='month',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='previous_month', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='previous_month', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='day',
                                        value=Subscript(
                                            value=Name(id='days_previous_month', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='company', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='old_fiscalyear_lock_date', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='fiscalyear_lock_date',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='old_period_lock_date', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='period_lock_date',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='old_tax_lock_date', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='tax_lock_date',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='old_tax_lock_date', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='tax_lock_date', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Constant(value='tax_lock_date', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
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
                                                        args=[Constant(value="The tax lock date is irreversible and can't be removed.", kind=None)],
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='old_tax_lock_date', ctx=Load()),
                                            Name(id='tax_lock_date', ctx=Load()),
                                            Compare(
                                                left=Name(id='tax_lock_date', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Name(id='old_tax_lock_date', ctx=Load())],
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
                                                        args=[Constant(value='The new tax lock date must be set after the previous lock date.', kind=None)],
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
                                    targets=[Name(id='tax_lock_date', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='tax_lock_date', ctx=Load()),
                                            Name(id='old_tax_lock_date', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='tax_lock_date', ctx=Load()),
                                            Compare(
                                                left=Name(id='tax_lock_date', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Name(id='previous_month', ctx=Load())],
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
                                                        args=[Constant(value='You cannot lock a period that has not yet ended. Therefore, the tax lock date must be anterior (or equal) to the last day of the previous month.', kind=None)],
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='old_fiscalyear_lock_date', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='fiscalyear_lock_date', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Constant(value='fiscalyear_lock_date', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
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
                                                        args=[Constant(value="The lock date for advisors is irreversible and can't be removed.", kind=None)],
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='old_fiscalyear_lock_date', ctx=Load()),
                                            Name(id='fiscalyear_lock_date', ctx=Load()),
                                            Compare(
                                                left=Name(id='fiscalyear_lock_date', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Name(id='old_fiscalyear_lock_date', ctx=Load())],
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
                                                        args=[Constant(value='Any new All Users Lock Date must be posterior (or equal) to the previous one.', kind=None)],
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
                                    targets=[Name(id='fiscalyear_lock_date', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='fiscalyear_lock_date', ctx=Load()),
                                            Name(id='old_fiscalyear_lock_date', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='fiscalyear_lock_date', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='fiscalyear_lock_date', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Name(id='previous_month', ctx=Load())],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You cannot lock a period that has not yet ended. Therefore, the All Users Lock Date must be anterior (or equal) to the last day of the previous month.', kind=None)],
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
                                    targets=[Name(id='period_lock_date', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='period_lock_date', ctx=Load()),
                                            Name(id='old_period_lock_date', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='period_lock_date', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='period_lock_date', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Name(id='fiscalyear_lock_date', ctx=Load())],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You cannot set stricter restrictions on advisors than on users. Therefore, the All Users Lock Date must be anterior (or equal) to the Invoice/Bills Lock Date.', kind=None)],
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
                    decorator_list=[],
                    returns=None,
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='fiscalyear_lock_date', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='period_lock_date', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='tax_lock_date', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_autorise_lock_date_changes',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResCompany', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
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
    ],
    type_ignores=[],
)
