Module(
    body=[
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='api', asname=None),
                alias(name='_', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='format_date', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='formatLang', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccruedExpenseRevenue',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account.accrued.orders.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Accrued Orders Wizard', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_account_domain',
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
                                left=Call(
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
                                    args=[Constant(value='active_model', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='purchase.order', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='user_type_id', kind=None),
                                                    Constant(value='=', kind=None),
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
                                                            args=[Constant(value='account.data_account_type_current_liabilities', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_default_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='user_type_id', kind=None),
                                                    Constant(value='=', kind=None),
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
                                                            args=[Constant(value='account.data_account_type_current_assets', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_default_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_default_company',
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
                                    args=[Constant(value='active_model', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='orders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='active_model', kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='active_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='orders', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Name(id='orders', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
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
                                arg='default',
                                value=Name(id='_get_default_company', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='journal_id', ctx=Store())],
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
                                value=Constant(value='account.journal', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_journal_id', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('type', '=', 'general'), ('company_id', '=', company_id)]", kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Journal', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='today',
                                    ctx=Load(),
                                ),
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
                    targets=[Name(id='reversal_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_reversal_date', kind=None),
                            ),
                            keyword(
                                arg='required',
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
                                arg='string',
                                value=Constant(value='Amount', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Specify an arbitrary value that will be accrued on a         default account for the entire order, regardless of the products on the different lines.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='currency_id', ctx=Store())],
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
                                value=Constant(value='company_id.currency_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Company Currency', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
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
                    targets=[Name(id='account_id', ctx=Store())],
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
                                value=Constant(value='account.account', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Accrual Account', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Name(id='_get_account_domain', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='preview_data', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_preview_data', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='display_amount', ctx=Store())],
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
                                value=Constant(value='_compute_display_amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_display_amount',
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
                            targets=[Name(id='single_order', ctx=Store())],
                            value=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='active_ids', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='preview_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='loads',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='preview_data',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='preview_data', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='groups_vals', kind=None),
                                                        List(elts=[], ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='items_vals', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='display_amount',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='single_order', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='lines', ctx=Load()),
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
                            args=[
                                Constant(value='date', kind=None),
                                Constant(value='amount', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_reversal_date',
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
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='reversal_date',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='reversal_date',
                                                    ctx=Load(),
                                                ),
                                                ops=[LtE()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='reversal_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='date',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='reversal_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='reversal_date',
                                                ctx=Load(),
                                            ),
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
                            args=[Constant(value='date', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_journal_id',
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
                            targets=[Name(id='journal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.journal', kind=None),
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
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='general', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
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
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='journal', ctx=Load()),
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
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_preview_data',
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
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='preview_vals', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Call(
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
                                                    attr='_move_dict_to_preview_vals',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='_compute_move_vals',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='currency_id',
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
                                Assign(
                                    targets=[Name(id='preview_columns', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='field', kind=None),
                                                    Constant(value='label', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='account_id', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Account', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='field', kind=None),
                                                    Constant(value='label', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='name', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Label', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='field', kind=None),
                                                    Constant(value='label', kind=None),
                                                    Constant(value='class', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='debit', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Debit', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='text-right text-nowrap', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='field', kind=None),
                                                    Constant(value='label', kind=None),
                                                    Constant(value='class', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='credit', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Credit', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='text-right text-nowrap', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='preview_data',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='groups_vals', kind=None),
                                                    Constant(value='options', kind=None),
                                                ],
                                                values=[
                                                    Name(id='preview_vals', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='columns', kind=None)],
                                                        values=[Name(id='preview_columns', ctx=Load())],
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='date', kind=None),
                                Constant(value='journal_id', kind=None),
                                Constant(value='account_id', kind=None),
                                Constant(value='amount', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_move_vals',
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
                        FunctionDef(
                            name='_get_aml_vals',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='order', annotation=None, type_comment=None),
                                    arg(arg='balance', annotation=None, type_comment=None),
                                    arg(arg='amount_currency', annotation=None, type_comment=None),
                                    arg(arg='account_id', annotation=None, type_comment=None),
                                    arg(arg='label', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Constant(value='', kind=None)],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='is_purchase', ctx=Load()),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='balance', ctx=Store()),
                                            op=Mult(),
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='amount_currency', ctx=Store()),
                                            op=Mult(),
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                            Constant(value='account_id', kind=None),
                                        ],
                                        values=[
                                            Name(id='label', ctx=Load()),
                                            IfExp(
                                                test=Compare(
                                                    left=Name(id='balance', ctx=Load()),
                                                    ops=[Gt()],
                                                    comparators=[Constant(value=0, kind=None)],
                                                ),
                                                body=Name(id='balance', ctx=Load()),
                                                orelse=Constant(value=0.0, kind=None),
                                            ),
                                            IfExp(
                                                test=Compare(
                                                    left=Name(id='balance', ctx=Load()),
                                                    ops=[Lt()],
                                                    comparators=[Constant(value=0, kind=None)],
                                                ),
                                                body=BinOp(
                                                    left=Name(id='balance', ctx=Load()),
                                                    op=Mult(),
                                                    right=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                ),
                                                orelse=Constant(value=0.0, kind=None),
                                            ),
                                            Name(id='account_id', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='order', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='currency_id',
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
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='amount_currency', kind=None),
                                                            Constant(value='currency_id', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='amount_currency', ctx=Load()),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='order', ctx=Load()),
                                                                    attr='currency_id',
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
                            name='_ellipsis',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='string', annotation=None, type_comment=None),
                                    arg(arg='size', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='string', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Name(id='size', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Name(id='string', ctx=Load()),
                                                    slice=Slice(
                                                        lower=Constant(value=0, kind=None),
                                                        upper=BinOp(
                                                            left=Name(id='size', ctx=Load()),
                                                            op=Sub(),
                                                            right=Constant(value=3, kind=None),
                                                        ),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='...', kind=None),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='string', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
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
                            targets=[Name(id='move_lines', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_purchase', ctx=Store())],
                            value=Compare(
                                left=Call(
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
                                    args=[Constant(value='active_model', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='purchase.order', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='orders', ctx=Store())],
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
                                                slice=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='active_model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='active_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='orders', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='o', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='o', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Entries can only be created for a single company at a time.', kind=None)],
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
                            targets=[Name(id='orders_with_entries', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fnames', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total_balance', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='orders', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='orders', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='total_balance', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='order_line', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='order_line',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='is_purchase', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='account', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='order_line', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='property_account_expense_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='categ_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='property_account_expense_categ_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='account', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='order_line', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='property_account_income_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='categ_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='property_account_income_categ_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_get_aml_vals', ctx=Load()),
                                                args=[
                                                    Name(id='order', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='amount',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                    Attribute(
                                                        value=Name(id='account', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='label',
                                                        value=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Manual entry', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='move_lines', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='values', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='other_currency', ctx=Store())],
                                            value=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='rate', ctx=Store())],
                                            value=IfExp(
                                                test=Name(id='other_currency', ctx=Load()),
                                                body=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='order', ctx=Load()),
                                                                    attr='currency_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_get_rates',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='date',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='order', ctx=Load()),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                orelse=Constant(value=1.0, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='o', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='origin',
                                                        value=Name(id='order', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='is_purchase', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='o', ctx=Load()),
                                                                        attr='order_line',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='accrual_entry_date',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='_compute_qty_received',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='o', ctx=Load()),
                                                                        attr='order_line',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='accrual_entry_date',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='_compute_qty_invoiced',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='o', ctx=Load()),
                                                                        attr='order_line',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='accrual_entry_date',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='_compute_qty_delivered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='o', ctx=Load()),
                                                                        attr='order_line',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='accrual_entry_date',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='_compute_qty_invoiced',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='o', ctx=Load()),
                                                                        attr='order_line',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='accrual_entry_date',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='_compute_untaxed_amount_invoiced',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='o', ctx=Load()),
                                                                        attr='order_line',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='accrual_entry_date',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='_get_to_invoice_qty',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='lines', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='o', ctx=Load()),
                                                        attr='order_line',
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
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Float',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='compare',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='l', ctx=Load()),
                                                                        attr='qty_to_invoice',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=0, kind=None),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='precision_digits',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='l', ctx=Load()),
                                                                                attr='product_uom',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='rounding',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value=1, kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='order_line', ctx=Store()),
                                            iter=Name(id='lines', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Name(id='is_purchase', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='account', ctx=Store())],
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='property_account_expense_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='order_line', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='categ_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='property_account_expense_categ_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='amount', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='company_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='currency_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='round',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=BinOp(
                                                                            left=Attribute(
                                                                                value=Name(id='order_line', ctx=Load()),
                                                                                attr='qty_to_invoice',
                                                                                ctx=Load(),
                                                                            ),
                                                                            op=Mult(),
                                                                            right=Attribute(
                                                                                value=Name(id='order_line', ctx=Load()),
                                                                                attr='price_unit',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                        op=Div(),
                                                                        right=Name(id='rate', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='amount_currency', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='currency_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='round',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='qty_to_invoice',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Mult(),
                                                                        right=Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='price_unit',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='fnames', ctx=Store())],
                                                            value=List(
                                                                elts=[
                                                                    Constant(value='qty_to_invoice', kind=None),
                                                                    Constant(value='qty_received', kind=None),
                                                                    Constant(value='qty_invoiced', kind=None),
                                                                    Constant(value='invoice_lines', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='label', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='%s - %s; %s Billed, %s Received at %s each', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='order', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='_ellipsis', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='order_line', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=20, kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='qty_invoiced',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='qty_received',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='formatLang', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='order_line', ctx=Load()),
                                                                                attr='price_unit',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='currency_obj',
                                                                                value=Attribute(
                                                                                    value=Name(id='order', ctx=Load()),
                                                                                    attr='currency_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='account', ctx=Store())],
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='property_account_income_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='order_line', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='categ_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='property_account_income_categ_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='amount', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='company_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='currency_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='round',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='untaxed_amount_to_invoice',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Div(),
                                                                        right=Name(id='rate', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='amount_currency', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='untaxed_amount_to_invoice',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='fnames', ctx=Store())],
                                                            value=List(
                                                                elts=[
                                                                    Constant(value='qty_to_invoice', kind=None),
                                                                    Constant(value='untaxed_amount_to_invoice', kind=None),
                                                                    Constant(value='qty_invoiced', kind=None),
                                                                    Constant(value='qty_delivered', kind=None),
                                                                    Constant(value='invoice_lines', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='label', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='%s - %s; %s Invoiced, %s Delivered at %s each', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='order', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='_ellipsis', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='order_line', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=20, kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='qty_invoiced',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='qty_delivered',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='formatLang', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='order_line', ctx=Load()),
                                                                                attr='price_unit',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='currency_obj',
                                                                                value=Attribute(
                                                                                    value=Name(id='order', ctx=Load()),
                                                                                    attr='currency_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                Assign(
                                                    targets=[Name(id='values', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_get_aml_vals', ctx=Load()),
                                                        args=[
                                                            Name(id='order', ctx=Load()),
                                                            Name(id='amount', ctx=Load()),
                                                            Name(id='amount_currency', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='account', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='label',
                                                                value=Name(id='label', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='move_lines', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='values', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='total_balance', ctx=Store()),
                                                    op=Add(),
                                                    value=Name(id='amount', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='order_line',
                                                        ctx=Load(),
                                                    ),
                                                    attr='invalidate_cache',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='fnames',
                                                        value=Name(id='fnames', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='is_zero',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='total_balance', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_get_aml_vals', ctx=Load()),
                                        args=[
                                            Name(id='orders', ctx=Load()),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Name(id='total_balance', ctx=Load()),
                                            ),
                                            Constant(value=0.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='label',
                                                value=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Accrued total', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move_lines', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Command', ctx=Load()),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='move_type', ctx=Store())],
                            value=IfExp(
                                test=Name(id='is_purchase', ctx=Load()),
                                body=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='Expense', kind=None)],
                                    keywords=[],
                                ),
                                orelse=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='Revenue', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='ref', kind=None),
                                    Constant(value='journal_id', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='line_ids', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='Accrued %s entry as of %s', kind=None),
                                            Name(id='move_type', ctx=Load()),
                                            Call(
                                                func=Name(id='format_date', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='date',
                                        ctx=Load(),
                                    ),
                                    Name(id='move_lines', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='move_vals', ctx=Load()),
                                    Name(id='orders_with_entries', ctx=Load()),
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
                    name='create_entries',
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
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='reversal_date',
                                    ctx=Load(),
                                ),
                                ops=[LtE()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='date',
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
                                                args=[Constant(value='Reversal date must be posterior to date.', kind=None)],
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='move_vals', ctx=Store()),
                                        Name(id='orders_with_entries', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_move_vals',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move', ctx=Store())],
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
                                args=[Name(id='move_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move', ctx=Load()),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='reverse_move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move', ctx=Load()),
                                    attr='_reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default_values_list',
                                        value=List(
                                            elts=[
                                                Dict(
                                                    keys=[
                                                        Constant(value='ref', kind=None),
                                                        Constant(value='date', kind=None),
                                                    ],
                                                    values=[
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[
                                                                Constant(value='Reversal of: %s', kind=None),
                                                                Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='ref',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='reversal_date',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
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
                                    value=Name(id='reverse_move', ctx=Load()),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='orders_with_entries', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Accrual entry created on %s: <a href=# data-oe-model=account.move data-oe-id=%d>%s</a>.                    And its <a href=# data-oe-model=account.move data-oe-id=%d>reverse entry</a>.', kind=None)],
                                            keywords=[],
                                        ),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='date',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='reverse_move', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Name(id='body', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='domain', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Accrual Moves', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='account.move', kind=None),
                                    Constant(value='tree,form', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='reverse_move', ctx=Load()),
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
