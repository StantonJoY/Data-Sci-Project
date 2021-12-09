Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='date', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccountPartialReconcile',
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
                    value=Constant(value='account.partial.reconcile', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Partial Reconcile', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='debit_move_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='account.move.line', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
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
                    targets=[Name(id='credit_move_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='account.move.line', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
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
                    targets=[Name(id='full_reconcile_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='account.full.reconcile', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Full Reconcile', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='res.currency', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Company Currency', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.currency_id', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Utility field to express amount currency', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='debit_currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='res.currency', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_debit_currency_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Currency of the debit journal item.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='credit_currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='res.currency', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_credit_currency_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Currency of the credit journal item.', kind=None),
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
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='currency_field',
                                value=Constant(value='company_currency_id', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Always positive amount concerned by this matching expressed in the company currency.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='debit_amount_currency', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='currency_field',
                                value=Constant(value='debit_currency_id', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Always positive amount concerned by this matching expressed in the debit line foreign currency.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='credit_amount_currency', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='currency_field',
                                value=Constant(value='credit_currency_id', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Always positive amount concerned by this matching expressed in the credit line foreign currency.', kind=None),
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
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='res.company', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
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
                                arg='related',
                                value=Constant(value='debit_move_id.company_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='max_date', ctx=Store())],
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
                                value=Constant(value='Max Date of Matched Lines', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_max_date', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field used to determine at which date this reconciliation needs to be shown on the aged receivable/payable reports.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_required_computed_currencies',
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
                            targets=[Name(id='bad_partials', ctx=Store())],
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
                                            args=[arg(arg='partial', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='debit_currency_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='credit_currency_id',
                                                        ctx=Load(),
                                                    ),
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
                            test=Name(id='bad_partials', ctx=Load()),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Missing foreign currencies on partials having ids: %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='bad_partials', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='debit_currency_id', kind=None),
                                Constant(value='credit_currency_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_max_date',
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
                            target=Name(id='partial', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partial', ctx=Load()),
                                            attr='max_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='max', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partial', ctx=Load()),
                                                    attr='debit_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partial', ctx=Load()),
                                                    attr='credit_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='date',
                                                ctx=Load(),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='debit_move_id.date', kind=None),
                                Constant(value='credit_move_id.date', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_debit_currency_id',
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
                            target=Name(id='partial', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partial', ctx=Load()),
                                            attr='debit_currency_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partial', ctx=Load()),
                                                    attr='debit_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partial', ctx=Load()),
                                                    attr='debit_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='company_currency_id',
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
                            args=[Constant(value='debit_move_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_credit_currency_id',
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
                            target=Name(id='partial', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partial', ctx=Load()),
                                            attr='credit_currency_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partial', ctx=Load()),
                                                    attr='credit_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partial', ctx=Load()),
                                                    attr='credit_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='company_currency_id',
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
                            args=[Constant(value='credit_move_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                                operand=Name(id='self', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='full_to_unlink', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='full_reconcile_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='moves_to_reverse', ctx=Store())],
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
                                                    Constant(value='tax_cash_basis_rec_id', kind=None),
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
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='unlink',
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
                                    attr='context_today',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default_values_list', ctx=Store())],
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='date', kind=None),
                                        Constant(value='ref', kind=None),
                                    ],
                                    values=[
                                        IfExp(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='date',
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='period_lock_date',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='date', ctx=Load()),
                                                                attr='min',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            orelse=Name(id='today', ctx=Load()),
                                        ),
                                        BinOp(
                                            left=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Reversal of: %s', kind=None)],
                                                keywords=[],
                                            ),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='move', ctx=Store()),
                                        iter=Name(id='moves_to_reverse', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='moves_to_reverse', ctx=Load()),
                                    attr='_reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default_values_list', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='cancel',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='full_to_unlink', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                    name='_collect_tax_cash_basis_values',
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
                            value=Constant(value=" Collect all information needed to create the tax cash basis journal entries on the current partials.\n        :return:    A dictionary mapping each move_id to the result of 'account_move._collect_tax_cash_basis_values'.\n                    Also, add the 'partials' keys being a list of dictionary, one for each partial to process:\n                        * partial:          The account.partial.reconcile record.\n                        * percentage:       The reconciled percentage represented by the partial.\n                        * payment_rate:     The applied rate of this partial.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax_cash_basis_values_per_move', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='self', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='partial', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='move', ctx=Store()),
                                    iter=Set(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partial', ctx=Load()),
                                                    attr='debit_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partial', ctx=Load()),
                                                    attr='credit_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[Name(id='tax_cash_basis_values_per_move', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='tax_cash_basis_values_per_move', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='_collect_tax_cash_basis_values',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='tax_cash_basis_values_per_move', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='move_values', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='tax_cash_basis_values_per_move', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='journal', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='partial', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='tax_cash_basis_journal_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='journal', ctx=Load()),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value="There is no tax cash basis journal defined for the '%s' company.\nConfigure it in Accounting/Configuration/Settings", kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='partial', ctx=Load()),
                                                                        attr='company_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='display_name',
                                                                    ctx=Load(),
                                                                ),
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
                                            targets=[Name(id='partial_amount', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='partial_amount_currency', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='rate_amount', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='rate_amount_currency', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='debit_move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='move_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='move', ctx=Load())],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='partial_amount', ctx=Store()),
                                                    op=Add(),
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='amount',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='partial_amount_currency', ctx=Store()),
                                                    op=Add(),
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='debit_amount_currency',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='rate_amount', ctx=Store()),
                                                    op=Sub(),
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='partial', ctx=Load()),
                                                            attr='credit_move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='balance',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='rate_amount_currency', ctx=Store()),
                                                    op=Sub(),
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='partial', ctx=Load()),
                                                            attr='credit_move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='amount_currency',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='source_line', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='debit_move_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='counterpart_line', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='credit_move_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='credit_move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='move_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='move', ctx=Load())],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='partial_amount', ctx=Store()),
                                                    op=Add(),
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='amount',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='partial_amount_currency', ctx=Store()),
                                                    op=Add(),
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='credit_amount_currency',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='rate_amount', ctx=Store()),
                                                    op=Add(),
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='partial', ctx=Load()),
                                                            attr='debit_move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='balance',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='rate_amount_currency', ctx=Store()),
                                                    op=Add(),
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='partial', ctx=Load()),
                                                            attr='debit_move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='amount_currency',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='source_line', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='credit_move_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='counterpart_line', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='debit_move_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='move_values', ctx=Load()),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='percentage', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='partial_amount', ctx=Load()),
                                                        op=Div(),
                                                        right=Subscript(
                                                            value=Name(id='move_values', ctx=Load()),
                                                            slice=Constant(value='total_balance', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='percentage', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='partial_amount_currency', ctx=Load()),
                                                        op=Div(),
                                                        right=Subscript(
                                                            value=Name(id='move_values', ctx=Load()),
                                                            slice=Constant(value='total_amount_currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='source_line', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='counterpart_line', ctx=Load()),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='payment_rate', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.currency', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_get_conversion_rate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='counterpart_line', ctx=Load()),
                                                                attr='company_currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='source_line', ctx=Load()),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='counterpart_line', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='counterpart_line', ctx=Load()),
                                                                attr='date',
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
                                                    test=Name(id='rate_amount', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='payment_rate', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='rate_amount_currency', ctx=Load()),
                                                                op=Div(),
                                                                right=Name(id='rate_amount', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='payment_rate', ctx=Store())],
                                                            value=Constant(value=0.0, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='partial_vals', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='partial', kind=None),
                                                    Constant(value='percentage', kind=None),
                                                    Constant(value='payment_rate', kind=None),
                                                ],
                                                values=[
                                                    Name(id='partial', ctx=Load()),
                                                    Name(id='percentage', ctx=Load()),
                                                    Name(id='payment_rate', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='move_values', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='partials', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='move_values', ctx=Load()),
                                                        slice=Constant(value='partials', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='partial_vals', ctx=Load())],
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
                            value=DictComp(
                                key=Name(id='k', ctx=Load()),
                                value=Name(id='v', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='k', ctx=Store()),
                                                Name(id='v', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='tax_cash_basis_values_per_move', ctx=Load()),
                                                attr='items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='v', ctx=Load())],
                                        is_async=0,
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
                    name='_prepare_cash_basis_base_line_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='base_line', annotation=None, type_comment=None),
                            arg(arg='balance', annotation=None, type_comment=None),
                            arg(arg='amount_currency', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prepare the values to be used to create the cash basis journal items for the tax base line\n        passed as parameter.\n\n        :param base_line:       An account.move.line being the base of some taxes.\n        :param balance:         The balance to consider for this line.\n        :param amount_currency: The balance in foreign currency to consider for this line.\n        :return:                A python dictionary that could be passed to the create method of\n                                account.move.line.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='account', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='base_line', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='account_cash_basis_base_account_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='base_line', ctx=Load()),
                                        attr='account_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='base_line', ctx=Load()),
                                        attr='tax_ids',
                                        ctx=Load(),
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
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='tax_exigibility',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='on_payment', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_refund', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base_line', ctx=Load()),
                                    attr='belongs_to_refund',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tax_ids', ctx=Load()),
                                    attr='get_tax_tags',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='is_refund', ctx=Load()),
                                    Constant(value='base', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='base_line', ctx=Load()),
                                        attr='tax_tag_ids',
                                        ctx=Load(),
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
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='applicability',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='products', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='all_tags', ctx=Store())],
                            value=BinOp(
                                left=Name(id='tax_tags', ctx=Load()),
                                op=Add(),
                                right=Name(id='product_tags', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='tax_ids', kind=None),
                                    Constant(value='tax_tag_ids', kind=None),
                                    Constant(value='tax_tag_invert', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='base_line', ctx=Load()),
                                            attr='move_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    IfExp(
                                        test=Compare(
                                            left=Name(id='balance', ctx=Load()),
                                            ops=[Gt()],
                                            comparators=[Constant(value=0.0, kind=None)],
                                        ),
                                        body=Name(id='balance', ctx=Load()),
                                        orelse=Constant(value=0.0, kind=None),
                                    ),
                                    IfExp(
                                        test=Compare(
                                            left=Name(id='balance', ctx=Load()),
                                            ops=[Lt()],
                                            comparators=[Constant(value=0.0, kind=None)],
                                        ),
                                        body=UnaryOp(
                                            op=USub(),
                                            operand=Name(id='balance', ctx=Load()),
                                        ),
                                        orelse=Constant(value=0.0, kind=None),
                                    ),
                                    Name(id='amount_currency', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='base_line', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='base_line', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='account', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Command', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='tax_ids', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Command', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='all_tags', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='base_line', ctx=Load()),
                                        attr='tax_tag_invert',
                                        ctx=Load(),
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
                    name='_prepare_cash_basis_counterpart_base_line_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cb_base_line_vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prepare the move line used as a counterpart of the line created by\n        _prepare_cash_basis_base_line_vals.\n\n        :param cb_base_line_vals:   The line returned by _prepare_cash_basis_base_line_vals.\n        :return:                    A python dictionary that could be passed to the create method of\n                                    account.move.line.\n        ', kind=None),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=Name(id='cb_base_line_vals', ctx=Load()),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='cb_base_line_vals', ctx=Load()),
                                        slice=Constant(value='credit', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='cb_base_line_vals', ctx=Load()),
                                        slice=Constant(value='debit', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='cb_base_line_vals', ctx=Load()),
                                        slice=Constant(value='account_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Subscript(
                                            value=Name(id='cb_base_line_vals', ctx=Load()),
                                            slice=Constant(value='amount_currency', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Subscript(
                                        value=Name(id='cb_base_line_vals', ctx=Load()),
                                        slice=Constant(value='currency_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='cb_base_line_vals', ctx=Load()),
                                        slice=Constant(value='partner_id', kind=None),
                                        ctx=Load(),
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
                    name='_prepare_cash_basis_tax_line_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tax_line', annotation=None, type_comment=None),
                            arg(arg='balance', annotation=None, type_comment=None),
                            arg(arg='amount_currency', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prepare the move line corresponding to a tax in the cash basis entry.\n\n        :param tax_line:        An account.move.line record being a tax line.\n        :param balance:         The balance to consider for this line.\n        :param amount_currency: The balance in foreign currency to consider for this line.\n        :return:                A python dictionary that could be passed to the create method of\n                                account.move.line.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='tax_line', ctx=Load()),
                                        attr='tax_ids',
                                        ctx=Load(),
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
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='tax_exigibility',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='on_payment', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tax_ids', ctx=Load()),
                                    attr='get_tax_tags',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tax_line', ctx=Load()),
                                            attr='tax_repartition_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='refund_tax_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='tax_line', ctx=Load()),
                                        attr='tax_tag_ids',
                                        ctx=Load(),
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
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='applicability',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='products', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='all_tags', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='base_tags', ctx=Load()),
                                    op=Add(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='tax_line', ctx=Load()),
                                            attr='tax_repartition_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='tag_ids',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Name(id='product_tags', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='tax_base_amount', kind=None),
                                    Constant(value='tax_repartition_line_id', kind=None),
                                    Constant(value='tax_ids', kind=None),
                                    Constant(value='tax_tag_ids', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='tax_line', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    IfExp(
                                        test=Compare(
                                            left=Name(id='balance', ctx=Load()),
                                            ops=[Gt()],
                                            comparators=[Constant(value=0.0, kind=None)],
                                        ),
                                        body=Name(id='balance', ctx=Load()),
                                        orelse=Constant(value=0.0, kind=None),
                                    ),
                                    IfExp(
                                        test=Compare(
                                            left=Name(id='balance', ctx=Load()),
                                            ops=[Lt()],
                                            comparators=[Constant(value=0.0, kind=None)],
                                        ),
                                        body=UnaryOp(
                                            op=USub(),
                                            operand=Name(id='balance', ctx=Load()),
                                        ),
                                        orelse=Constant(value=0.0, kind=None),
                                    ),
                                    Attribute(
                                        value=Name(id='tax_line', ctx=Load()),
                                        attr='tax_base_amount',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tax_line', ctx=Load()),
                                            attr='tax_repartition_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Command', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='tax_ids', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Command', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='all_tags', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tax_line', ctx=Load()),
                                                        attr='tax_repartition_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='tax_line', ctx=Load()),
                                                    attr='account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Name(id='amount_currency', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tax_line', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tax_line', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
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
                    name='_prepare_cash_basis_counterpart_tax_line_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tax_line', annotation=None, type_comment=None),
                            arg(arg='cb_tax_line_vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prepare the move line used as a counterpart of the line created by\n        _prepare_cash_basis_tax_line_vals.\n\n        :param tax_line:            An account.move.line record being a tax line.\n        :param cb_tax_line_vals:    The result of _prepare_cash_basis_counterpart_tax_line_vals.\n        :return:                    A python dictionary that could be passed to the create method of\n                                    account.move.line.\n        ', kind=None),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=Name(id='cb_tax_line_vals', ctx=Load()),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='cb_tax_line_vals', ctx=Load()),
                                        slice=Constant(value='credit', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='cb_tax_line_vals', ctx=Load()),
                                        slice=Constant(value='debit', kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tax_line', ctx=Load()),
                                            attr='account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Subscript(
                                            value=Name(id='cb_tax_line_vals', ctx=Load()),
                                            slice=Constant(value='amount_currency', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Subscript(
                                        value=Name(id='cb_tax_line_vals', ctx=Load()),
                                        slice=Constant(value='currency_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='cb_tax_line_vals', ctx=Load()),
                                        slice=Constant(value='partner_id', kind=None),
                                        ctx=Load(),
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
                    name='_get_cash_basis_base_line_grouping_key_from_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='base_line_vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Get the grouping key of a cash basis base line that hasn't yet been created.\n        :param base_line_vals:  The values to create a new account.move.line record.\n        :return:                The grouping key as a tuple.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax_ids', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='base_line_vals', ctx=Load()),
                                        slice=Constant(value='tax_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=2, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_taxes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tax_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='base_line_vals', ctx=Load()),
                                        slice=Constant(value='currency_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='base_line_vals', ctx=Load()),
                                        slice=Constant(value='partner_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='base_line_vals', ctx=Load()),
                                        slice=Constant(value='account_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='base_taxes', ctx=Load()),
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
                                                            body=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='tax_exigibility',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='on_payment', kind=None)],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
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
                    name='_get_cash_basis_base_line_grouping_key_from_record',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='base_line', annotation=None, type_comment=None),
                            arg(arg='account', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get the grouping key of a journal item being a base line.\n        :param base_line:   An account.move.line record.\n        :param account:     Optional account to shadow the current base_line one.\n        :return:            The grouping key as a tuple.\n        ', kind=None),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='base_line', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='base_line', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='account', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='base_line', ctx=Load()),
                                                    attr='account_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='base_line', ctx=Load()),
                                                            attr='tax_ids',
                                                            ctx=Load(),
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
                                                            body=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='tax_exigibility',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='on_payment', kind=None)],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
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
                    name='_get_cash_basis_tax_line_grouping_key_from_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tax_line_vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Get the grouping key of a cash basis tax line that hasn't yet been created.\n        :param tax_line_vals:   The values to create a new account.move.line record.\n        :return:                The grouping key as a tuple.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax_ids', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='tax_line_vals', ctx=Load()),
                                        slice=Constant(value='tax_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=2, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_taxes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tax_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='tax_line_vals', ctx=Load()),
                                        slice=Constant(value='currency_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='tax_line_vals', ctx=Load()),
                                        slice=Constant(value='partner_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='tax_line_vals', ctx=Load()),
                                        slice=Constant(value='account_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='base_taxes', ctx=Load()),
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
                                                            body=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='tax_exigibility',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='on_payment', kind=None)],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='tax_line_vals', ctx=Load()),
                                        slice=Constant(value='tax_repartition_line_id', kind=None),
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
                    name='_get_cash_basis_tax_line_grouping_key_from_record',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tax_line', annotation=None, type_comment=None),
                            arg(arg='account', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get the grouping key of a journal item being a tax line.\n        :param tax_line:    An account.move.line record.\n        :param account:     Optional account to shadow the current tax_line one.\n        :return:            The grouping key as a tuple.\n        ', kind=None),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tax_line', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tax_line', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='account', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='tax_line', ctx=Load()),
                                                    attr='account_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='tax_line', ctx=Load()),
                                                            attr='tax_ids',
                                                            ctx=Load(),
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
                                                            body=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='tax_exigibility',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='on_payment', kind=None)],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tax_line', ctx=Load()),
                                            attr='tax_repartition_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
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
                    name='_create_tax_cash_basis_moves',
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
                            value=Constant(value=' Create the tax cash basis journal entries.\n        :return: The newly created journal entries.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax_cash_basis_values_per_move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_collect_tax_cash_basis_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='moves_to_create', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_reconcile_after', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move_values', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='tax_cash_basis_values_per_move', ctx=Load()),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='move', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='move_values', ctx=Load()),
                                        slice=Constant(value='move', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pending_cash_basis_lines', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='partial_values', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='move_values', ctx=Load()),
                                        slice=Constant(value='partials', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partial', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='partial_values', ctx=Load()),
                                                slice=Constant(value='partial', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='move_vals', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='date', kind=None),
                                                    Constant(value='ref', kind=None),
                                                    Constant(value='journal_id', kind=None),
                                                    Constant(value='line_ids', kind=None),
                                                    Constant(value='tax_cash_basis_rec_id', kind=None),
                                                    Constant(value='tax_cash_basis_origin_move_id', kind=None),
                                                    Constant(value='fiscal_position_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='entry', kind=None),
                                                    Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='max_date',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='partial', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tax_cash_basis_journal_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='partial', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='fiscal_position_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='partial_lines_to_create', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='caba_treatment', ctx=Store()),
                                                    Name(id='line', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Subscript(
                                                value=Name(id='move_values', ctx=Load()),
                                                slice=Constant(value='to_process_lines', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='amount_currency', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='round',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='amount_currency',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Mult(),
                                                                right=Subscript(
                                                                    value=Name(id='partial_values', ctx=Load()),
                                                                    slice=Constant(value='percentage', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='balance', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Subscript(
                                                                        value=Name(id='partial_values', ctx=Load()),
                                                                        slice=Constant(value='payment_rate', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    BinOp(
                                                                        left=Name(id='amount_currency', ctx=Load()),
                                                                        op=Div(),
                                                                        right=Subscript(
                                                                            value=Name(id='partial_values', ctx=Load()),
                                                                            slice=Constant(value='payment_rate', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=0.0, kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='caba_treatment', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='tax', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='cb_line_vals', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_prepare_cash_basis_tax_line_vals',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='line', ctx=Load()),
                                                                    Name(id='balance', ctx=Load()),
                                                                    Name(id='amount_currency', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='grouping_key', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_get_cash_basis_tax_line_grouping_key_from_vals',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='cb_line_vals', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='caba_treatment', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='base', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='cb_line_vals', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_prepare_cash_basis_base_line_vals',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='line', ctx=Load()),
                                                                            Name(id='balance', ctx=Load()),
                                                                            Name(id='amount_currency', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='grouping_key', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_get_cash_basis_base_line_grouping_key_from_vals',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='cb_line_vals', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='grouping_key', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='partial_lines_to_create', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='aggregated_vals', ctx=Store())],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='partial_lines_to_create', ctx=Load()),
                                                                    slice=Name(id='grouping_key', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='vals', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='debit', ctx=Store())],
                                                            value=BinOp(
                                                                left=Subscript(
                                                                    value=Name(id='aggregated_vals', ctx=Load()),
                                                                    slice=Constant(value='debit', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Name(id='cb_line_vals', ctx=Load()),
                                                                    slice=Constant(value='debit', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='credit', ctx=Store())],
                                                            value=BinOp(
                                                                left=Subscript(
                                                                    value=Name(id='aggregated_vals', ctx=Load()),
                                                                    slice=Constant(value='credit', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Name(id='cb_line_vals', ctx=Load()),
                                                                    slice=Constant(value='credit', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='balance', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='debit', ctx=Load()),
                                                                op=Sub(),
                                                                right=Name(id='credit', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='aggregated_vals', ctx=Load()),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='amount_currency', kind=None),
                                                                        ],
                                                                        values=[
                                                                            IfExp(
                                                                                test=Compare(
                                                                                    left=Name(id='balance', ctx=Load()),
                                                                                    ops=[Gt()],
                                                                                    comparators=[Constant(value=0, kind=None)],
                                                                                ),
                                                                                body=Name(id='balance', ctx=Load()),
                                                                                orelse=Constant(value=0, kind=None),
                                                                            ),
                                                                            IfExp(
                                                                                test=Compare(
                                                                                    left=Name(id='balance', ctx=Load()),
                                                                                    ops=[Lt()],
                                                                                    comparators=[Constant(value=0, kind=None)],
                                                                                ),
                                                                                body=UnaryOp(
                                                                                    op=USub(),
                                                                                    operand=Name(id='balance', ctx=Load()),
                                                                                ),
                                                                                orelse=Constant(value=0, kind=None),
                                                                            ),
                                                                            BinOp(
                                                                                left=Subscript(
                                                                                    value=Name(id='aggregated_vals', ctx=Load()),
                                                                                    slice=Constant(value='amount_currency', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Subscript(
                                                                                    value=Name(id='cb_line_vals', ctx=Load()),
                                                                                    slice=Constant(value='amount_currency', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='caba_treatment', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='tax', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='aggregated_vals', ctx=Load()),
                                                                            attr='update',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[Constant(value='tax_base_amount', kind=None)],
                                                                                values=[
                                                                                    BinOp(
                                                                                        left=Subscript(
                                                                                            value=Name(id='aggregated_vals', ctx=Load()),
                                                                                            slice=Constant(value='tax_base_amount', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Subscript(
                                                                                            value=Name(id='cb_line_vals', ctx=Load()),
                                                                                            slice=Constant(value='tax_base_amount', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                AugAssign(
                                                                    target=Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='partial_lines_to_create', ctx=Load()),
                                                                            slice=Name(id='grouping_key', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='tax_line', kind=None),
                                                                        ctx=Store(),
                                                                    ),
                                                                    op=Add(),
                                                                    value=Name(id='line', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='partial_lines_to_create', ctx=Load()),
                                                                    slice=Name(id='grouping_key', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Dict(
                                                                keys=[Constant(value='vals', kind=None)],
                                                                values=[Name(id='cb_line_vals', ctx=Load())],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='caba_treatment', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='tax', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='partial_lines_to_create', ctx=Load()),
                                                                                slice=Name(id='grouping_key', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='update',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[Constant(value='tax_line', kind=None)],
                                                                                values=[Name(id='line', ctx=Load())],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
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
                                        Assign(
                                            targets=[Name(id='sequence', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='grouping_key', ctx=Store()),
                                                    Name(id='aggregated_vals', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='partial_lines_to_create', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='line_vals', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='aggregated_vals', ctx=Load()),
                                                        slice=Constant(value='vals', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='line_vals', ctx=Load()),
                                                            slice=Constant(value='sequence', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='sequence', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='pending_cash_basis_lines', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='grouping_key', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='line_vals', ctx=Load()),
                                                                        slice=Constant(value='amount_currency', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Constant(value='tax_repartition_line_id', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='line_vals', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='tax_line', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='aggregated_vals', ctx=Load()),
                                                                slice=Constant(value='tax_line', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='counterpart_line_vals', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_prepare_cash_basis_counterpart_tax_line_vals',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='tax_line', ctx=Load()),
                                                                    Name(id='line_vals', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='counterpart_line_vals', ctx=Load()),
                                                                    slice=Constant(value='sequence', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BinOp(
                                                                left=Name(id='sequence', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='tax_line', ctx=Load()),
                                                                    attr='account_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='reconcile',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='move_index', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='len', ctx=Load()),
                                                                        args=[Name(id='moves_to_create', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='to_reconcile_after', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Name(id='tax_line', ctx=Load()),
                                                                                    Name(id='move_index', ctx=Load()),
                                                                                    Subscript(
                                                                                        value=Name(id='counterpart_line_vals', ctx=Load()),
                                                                                        slice=Constant(value='sequence', kind=None),
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
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='counterpart_line_vals', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_prepare_cash_basis_counterpart_base_line_vals',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='line_vals', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='counterpart_line_vals', ctx=Load()),
                                                                    slice=Constant(value='sequence', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BinOp(
                                                                left=Name(id='sequence', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                AugAssign(
                                                    target=Name(id='sequence', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=2, kind=None),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='move_vals', ctx=Load()),
                                                        slice=Constant(value='line_ids', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Name(id='counterpart_line_vals', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Name(id='line_vals', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='moves_to_create', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='move_vals', ctx=Load())],
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
                        Assign(
                            targets=[Name(id='moves', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='moves_to_create', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='moves', ctx=Load()),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='soft',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='lines', ctx=Store()),
                                    Name(id='move_index', ctx=Store()),
                                    Name(id='sequence', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='to_reconcile_after', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
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
                                                body=UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='reconciled',
                                                        ctx=Load(),
                                                    ),
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
                                        operand=Name(id='lines', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='counterpart_line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='moves', ctx=Load()),
                                                    slice=Name(id='move_index', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
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
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='sequence',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='sequence', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='counterpart_line', ctx=Load()),
                                        attr='reconciled',
                                        ctx=Load(),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='lines', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='counterpart_line', ctx=Load()),
                                            ),
                                            attr='reconcile',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='moves', ctx=Load()),
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
