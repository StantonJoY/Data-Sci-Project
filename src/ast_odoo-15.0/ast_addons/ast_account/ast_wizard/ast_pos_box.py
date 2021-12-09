Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
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
            name='CashBox',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_register', ctx=Store())],
                    value=Constant(value=False, kind=None),
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
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Reason', kind=None),
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
                    targets=[Name(id='amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Amount', kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value=0, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='run',
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
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='active_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='active_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='active_ids', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='active_model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='active_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run',
                                    ctx=Load(),
                                ),
                                args=[Name(id='records', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='box', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='journal_id',
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
                                                                args=[Constant(value="Please check that the field 'Journal' is set on the Bank Statement", kind=None)],
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
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='journal_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='transfer_account_id',
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
                                                                args=[Constant(value="Please check that the field 'Transfer Account' is set on the company.", kind=None)],
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='box', ctx=Load()),
                                                    attr='_create_bank_statement_line',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='record', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_bank_statement_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='box', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='confirm', kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You cannot put/take money in/out for a bank statement which is closed.', kind=None)],
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
                                            value=Name(id='box', ctx=Load()),
                                            attr='_calculate_values_for_statement_line',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='record', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='account', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='transfer_account_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
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
                                                                slice=Constant(value='account.bank.statement.line', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='counterpart_account_id',
                                                                value=Attribute(
                                                                    value=Name(id='account', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='CashBoxOut',
            bases=[Name(id='CashBox', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='cash.box.out', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Cash Box Out', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_calculate_values_for_statement_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
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
                                operand=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='transfer_account_id',
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
                                                args=[Constant(value="You have to define an 'Internal Transfer Account' in your cash register's journal.", kind=None)],
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
                            targets=[Name(id='amount', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='date', kind=None),
                                    Constant(value='statement_id', kind=None),
                                    Constant(value='journal_id', kind=None),
                                    Constant(value='amount', kind=None),
                                    Constant(value='payment_ref', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='date',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='amount', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
