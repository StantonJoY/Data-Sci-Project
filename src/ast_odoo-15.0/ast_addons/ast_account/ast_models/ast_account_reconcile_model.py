Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='Command', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_is_zero', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[alias(name='get_unaccent_wrapper', asname=None)],
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
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='math',
            names=[alias(name='copysign', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='html2text', asname=None)],
        ),
        ClassDef(
            name='AccountReconcileModelPartnerMapping',
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
                    value=Constant(value='account.reconcile.model.partner.mapping', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Partner mapping for reconciliation models', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model_id', ctx=Store())],
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
                                value=Constant(value='account.reconcile.model', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
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
                                arg='comodel_name',
                                value=Constant(value='res.partner', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Partner', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='payment_ref_regex', ctx=Store())],
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
                                value=Constant(value='Find Text in Label', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='narration_regex', ctx=Store())],
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
                                value=Constant(value='Find Text in Notes', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='validate_regex',
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
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='narration_regex',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='payment_ref_regex',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Please set at least one of the match texts to create a partner mapping.', kind=None)],
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
                                Try(
                                    body=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='payment_ref_regex',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='current_regex', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='payment_ref_regex',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='re', ctx=Load()),
                                                            attr='compile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='payment_ref_regex',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='narration_regex',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='current_regex', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='narration_regex',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='re', ctx=Load()),
                                                            attr='compile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='narration_regex',
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
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='re', ctx=Load()),
                                                attr='error',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='The following regular expression is invalid to create a partner mapping: %s', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Name(id='current_regex', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
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
                            args=[
                                Constant(value='narration_regex', kind=None),
                                Constant(value='payment_ref_regex', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AccountReconcileModelLine',
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
                    value=Constant(value='account.reconcile.model.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Rules for the reconciliation model', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_check_company_auto', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.reconcile.model', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='allow_payment_tolerance', ctx=Store())],
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
                                value=Constant(value='model_id.allow_payment_tolerance', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='payment_tolerance_param', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='model_id.payment_tolerance_param', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rule_type', ctx=Store())],
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
                                value=Constant(value='model_id.rule_type', kind=None),
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
                                arg='related',
                                value=Constant(value='model_id.company_id', kind=None),
                            ),
                            keyword(
                                arg='store',
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
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
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
                        args=[Constant(value='account.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Account', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('deprecated', '=', False), ('company_id', '=', company_id), ('is_off_balance', '=', False)]", kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
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
                        args=[Constant(value='account.journal', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Journal', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('type', '=', 'general'), ('company_id', '=', company_id)]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field is ignored in a bank statement reconciliation.', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='label', ctx=Store())],
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
                                value=Constant(value='Journal Item Label', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='amount_type', ctx=Store())],
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
                                            Constant(value='fixed', kind=None),
                                            Constant(value='Fixed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='percentage', kind=None),
                                            Constant(value='Percentage of balance', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='percentage_st_line', kind=None),
                                            Constant(value='Percentage of statement line', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='regex', kind=None),
                                            Constant(value='From label', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='percentage', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='show_force_tax_included', ctx=Store())],
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
                                value=Constant(value='_compute_show_force_tax_included', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field used to show the force tax included button', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='force_tax_included', ctx=Store())],
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
                                value=Constant(value='Tax Included in Price', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Force the tax to be managed as a price included tax.', kind=None),
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
                                value=Constant(value='Float Amount', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_float_amount', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Technical shortcut to parse the amount to a float', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='amount_string', ctx=Store())],
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
                                value=Constant(value='Amount', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='100', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Value for the amount of the writeoff line\n    * Percentage: Percentage of the balance, between 0 and 100.\n    * Fixed: The fixed value of the writeoff. The amount will count as a debit if it is negative, as a credit if it is positive.\n    * From Label: There is no need for regex delimiter, only the regex is needed. For instance if you want to extract the amount from\nR:9672938 10/07 AX 9415126318 T:5L:NA BRT: 3358,07 C:\nYou could enter\nBRT: ([\\d,]+)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tax_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.tax', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Taxes', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='analytic_account_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.analytic.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Analytic Account', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='set null', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='analytic_tag_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.analytic.tag', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Analytic Tags', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='relation',
                                value=Constant(value='account_reconcile_model_analytic_tag_rel', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_tax_ids',
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
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='force_tax_included',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='tax_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_show_force_tax_included',
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
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='show_force_tax_included',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Compare(
                                            left=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='tax_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(value=1, kind=None)],
                                        ),
                                        body=Constant(value=False, kind=None),
                                        orelse=Constant(value=True, kind=None),
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
                            args=[Constant(value='tax_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_amount_type',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='amount_string',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='amount_type',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='percentage', kind=None),
                                            Constant(value='percentage_st_line', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='amount_string',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='100', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='amount_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='regex', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='amount_string',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='([\\d,]+)', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='amount_type', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_float_amount',
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
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='float', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='amount_string',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='amount',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=0, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
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
                            args=[Constant(value='amount_string', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_validate_amount',
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
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='amount_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='fixed', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
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
                                                        args=[Constant(value='The amount is not a number', kind=None)],
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
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='amount_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='percentage_st_line', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
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
                                                        args=[Constant(value="Balance percentage can't be 0", kind=None)],
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
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='amount_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='percentage', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
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
                                                        args=[Constant(value="Statement line percentage can't be 0", kind=None)],
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
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='amount_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='regex', kind=None)],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='re', ctx=Load()),
                                                            attr='compile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='amount_string',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='error',
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='The regex is not valid', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
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
                            args=[Constant(value='amount_string', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AccountReconcileModel',
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
                    value=Constant(value='account.reconcile.model', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Preset to create journal entries during a invoices and payments matching', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='mail.thread', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_check_company_auto', ctx=Store())],
                    value=Constant(value=True, kind=None),
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
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
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
                                value=Constant(value='Name', kind=None),
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
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
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
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
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
                    targets=[Name(id='rule_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='writeoff_button', kind=None),
                                                Constant(value='Button to generate counterpart entry', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='writeoff_suggestion', kind=None),
                                                Constant(value='Rule to suggest counterpart entry', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='invoice_matching', kind=None),
                                                Constant(value='Rule to match invoices/bills', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Type', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='writeoff_button', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='auto_reconcile', ctx=Store())],
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
                                value=Constant(value='Auto-validate', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Validate the statement line automatically (reconciliation based on your rule).', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='to_check', ctx=Store())],
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
                                value=Constant(value='To Check', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This matching rule is used when the user is not certain of all the information of the counterpart.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='matching_order', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='old_first', kind=None),
                                                Constant(value='Oldest first', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='new_first', kind=None),
                                                Constant(value='Newest first', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='old_first', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_text_location_label', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Search in the Statement's Label to find the Invoice/Payment's reference", kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_text_location_note', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Search in the Statement's Note to find the Invoice/Payment's reference", kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_text_location_reference', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Search in the Statement's Reference to find the Invoice/Payment's reference", kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_journal_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.journal', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Journals Availability', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('type', 'in', ('bank', 'cash')), ('company_id', '=', company_id)]", kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The reconciliation model will only be available from the selected journals.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_nature', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='amount_received', kind=None),
                                                Constant(value='Received', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='amount_paid', kind=None),
                                                Constant(value='Paid', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='both', kind=None),
                                                Constant(value='Paid/Received', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Amount Type', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='both', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The reconciliation model will only be applied to the selected transaction type:\n        * Amount Received: Only applied when receiving an amount.\n        * Amount Paid: Only applied when paying an amount.\n        * Amount Paid/Received: Applied in both cases.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='lower', kind=None),
                                                Constant(value='Is Lower Than', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='greater', kind=None),
                                                Constant(value='Is Greater Than', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='between', kind=None),
                                                Constant(value='Is Between', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Amount Condition', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The reconciliation model will only be applied when the amount being lower than, greater than or between specified amount(s).', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_amount_min', ctx=Store())],
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
                                value=Constant(value='Amount Min Parameter', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_amount_max', ctx=Store())],
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
                                value=Constant(value='Amount Max Parameter', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_label', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='contains', kind=None),
                                                Constant(value='Contains', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='not_contains', kind=None),
                                                Constant(value='Not Contains', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='match_regex', kind=None),
                                                Constant(value='Match Regex', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Label', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The reconciliation model will only be applied when the label:\n        * Contains: The proposition label must contains this string (case insensitive).\n        * Not Contains: Negation of "Contains".\n        * Match Regex: Define your own regular expression.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_label_param', ctx=Store())],
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
                                value=Constant(value='Label Parameter', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_note', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='contains', kind=None),
                                                Constant(value='Contains', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='not_contains', kind=None),
                                                Constant(value='Not Contains', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='match_regex', kind=None),
                                                Constant(value='Match Regex', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Note', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The reconciliation model will only be applied when the note:\n        * Contains: The proposition note must contains this string (case insensitive).\n        * Not Contains: Negation of "Contains".\n        * Match Regex: Define your own regular expression.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_note_param', ctx=Store())],
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
                                value=Constant(value='Note Parameter', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_transaction_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='contains', kind=None),
                                                Constant(value='Contains', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='not_contains', kind=None),
                                                Constant(value='Not Contains', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='match_regex', kind=None),
                                                Constant(value='Match Regex', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Transaction Type', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The reconciliation model will only be applied when the transaction type:\n        * Contains: The proposition transaction type must contains this string (case insensitive).\n        * Not Contains: Negation of "Contains".\n        * Match Regex: Define your own regular expression.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_transaction_type_param', ctx=Store())],
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
                                value=Constant(value='Transaction Type Parameter', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_same_currency', ctx=Store())],
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
                                value=Constant(value='Same Currency', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Restrict to propositions having the same currency as the statement line.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='allow_payment_tolerance', ctx=Store())],
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
                                value=Constant(value='Payment Tolerance', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Difference accepted in case of underpayment.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='payment_tolerance_param', ctx=Store())],
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
                                value=Constant(value='Gap', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_payment_tolerance_param', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The sum of total residual amount propositions matches the statement line amount under this amount/percentage.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='payment_tolerance_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='percentage', kind=None),
                                                Constant(value='in percentage', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='fixed_amount', kind=None),
                                                Constant(value='in amount', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='percentage', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The sum of total residual amount propositions and the statement line amount allowed gap type.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_partner', ctx=Store())],
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
                                value=Constant(value='Partner should be set', kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The reconciliation model will only be applied when a customer/vendor is set.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_partner_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Only Those Partners', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The reconciliation model will only be applied to the selected customers/vendors.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match_partner_category_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner.category', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Only Those Partner Categories', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The reconciliation model will only be applied to the selected customer/vendor categories.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.reconcile.model.line', kind=None),
                            Constant(value='model_id', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_mapping_line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Partner Mapping Lines', kind=None),
                            ),
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='account.reconcile.model.partner.mapping', kind=None),
                            ),
                            keyword(
                                arg='inverse_name',
                                value=Constant(value='model_id', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The mapping uses regular expressions.\n- To Match the text at the beginning of the line (in label or notes), simply fill in your text.\n- To Match the text anywhere (in label or notes), put your text between .*\n  e.g: .*N°48748 abc123.*', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='past_months_limit', ctx=Store())],
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
                                value=Constant(value='Search Months Limit', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=18, kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Number of months in the past to consider entries from when applying this model.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='decimal_separator', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
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
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.lang', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='_lang_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lang',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='decimal_point',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Every character that is nor a digit nor this separator will be removed from the matching string', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='show_decimal_separator', ctx=Store())],
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
                                value=Constant(value='_compute_show_decimal_separator', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field to decide if we should show the decimal separator for the regex matching field.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='number_entries', ctx=Store())],
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
                                value=Constant(value='Number of entries related to this model', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_number_entries', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_reconcile_stat',
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
                                args=[Constant(value='account.action_move_journal_line', kind=None)],
                                keywords=[],
                            ),
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
                                    Constant(value='\n            SELECT ARRAY_AGG(DISTINCT move_id)\n            FROM account_move_line\n            WHERE reconcile_model_id = %s\n        ', kind=None),
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
                                keywords=[],
                            ),
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
                                            Constant(value='help', kind=None),
                                        ],
                                        values=[
                                            Dict(keys=[], values=[]),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_cr',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='fetchone',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='<p class="o_view_nocontent_empty_folder">{}</p>', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='This reconciliation model has created no entry so far', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                    name='_compute_number_entries',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move.line', kind=None),
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
                                                    Constant(value='reconcile_model_id', kind=None),
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
                                        elts=[Constant(value='reconcile_model_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Constant(value='reconcile_model_id', kind=None),
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
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='d', ctx=Load()),
                                                        slice=Constant(value='reconcile_model_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='d', ctx=Load()),
                                                    slice=Constant(value='reconcile_model_id_count', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='d', ctx=Store()),
                                                iter=Name(id='data', ctx=Load()),
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
                            target=Name(id='model', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='number_entries',
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
                                                value=Name(id='model', ctx=Load()),
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
                    name='_compute_show_decimal_separator',
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
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='show_decimal_separator',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='amount_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='regex', kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='l', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='line_ids',
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='line_ids.amount_type', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_payment_tolerance_param',
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
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='payment_tolerance_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='percentage', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='payment_tolerance_param',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Constant(value=100.0, kind=None),
                                                    Call(
                                                        func=Name(id='max', ctx=Load()),
                                                        args=[
                                                            Constant(value=0.0, kind=None),
                                                            Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='payment_tolerance_param',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='payment_tolerance_param',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='max', ctx=Load()),
                                                args=[
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='payment_tolerance_param',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
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
                            args=[
                                Constant(value='payment_tolerance_param', kind=None),
                                Constant(value='payment_tolerance_type', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_payment_tolerance_param',
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
                                    test=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='allow_payment_tolerance',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='payment_tolerance_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='percentage', kind=None)],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Compare(
                                                            left=Constant(value=0, kind=None),
                                                            ops=[
                                                                LtE(),
                                                                LtE(),
                                                            ],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='payment_tolerance_param',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value=100, kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='A payment tolerance defined as a percentage should always be between 0 and 100', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='payment_tolerance_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='fixed_amount', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='payment_tolerance_param',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Lt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValidationError', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='A payment tolerance defined as an amount should always be higher than 0', kind=None)],
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
                            args=[
                                Constant(value='allow_payment_tolerance', kind=None),
                                Constant(value='payment_tolerance_param', kind=None),
                                Constant(value='payment_tolerance_type', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_taxes_move_lines_dict',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tax', annotation=None, type_comment=None),
                            arg(arg='base_line_dict', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get move.lines dict (to be passed to the create()) corresponding to a tax.\n        :param tax:             An account.tax record.\n        :param base_line_dict:  A dict representing the move.line containing the base amount.\n        :return: A list of dict representing move.lines to be created corresponding to the tax.\n        ', kind=None),
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
                            targets=[Name(id='balance', ctx=Store())],
                            value=Subscript(
                                value=Name(id='base_line_dict', ctx=Load()),
                                slice=Constant(value='balance', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_type', ctx=Store())],
                            value=Attribute(
                                value=Name(id='tax', ctx=Load()),
                                attr='type_tax_use',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_refund', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='tax_type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='sale', kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='balance', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='tax_type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='purchase', kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='balance', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tax', ctx=Load()),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Name(id='balance', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='is_refund',
                                        value=Name(id='is_refund', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_aml_dicts', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='tax_res', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='res', ctx=Load()),
                                slice=Constant(value='taxes', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tax', ctx=Store())],
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
                                        args=[
                                            Subscript(
                                                value=Name(id='tax_res', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='balance', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='tax_res', ctx=Load()),
                                        slice=Constant(value='amount', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='new_aml_dicts', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='balance', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='analytic_account_id', kind=None),
                                                    Constant(value='analytic_tag_ids', kind=None),
                                                    Constant(value='tax_repartition_line_id', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_tag_ids', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='reconcile_model_id', kind=None),
                                                ],
                                                values=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='tax_res', ctx=Load()),
                                                                slice=Constant(value='account_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='base_line_dict', ctx=Load()),
                                                                slice=Constant(value='account_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='tax_res', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='base_line_dict', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='partner_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(id='balance', ctx=Load()),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='balance', ctx=Load()),
                                                                        ops=[Gt()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    Name(id='balance', ctx=Load()),
                                                                ],
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='balance', ctx=Load()),
                                                                        ops=[Lt()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Name(id='balance', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='tax', ctx=Load()),
                                                                attr='analytic',
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='base_line_dict', ctx=Load()),
                                                                slice=Constant(value='analytic_account_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='tax', ctx=Load()),
                                                                attr='analytic',
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='base_line_dict', ctx=Load()),
                                                                slice=Constant(value='analytic_tag_ids', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='tax_res', ctx=Load()),
                                                        slice=Constant(value='tax_repartition_line_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Subscript(
                                                                        value=Name(id='tax_res', ctx=Load()),
                                                                        slice=Constant(value='tax_ids', kind=None),
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
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Subscript(
                                                                        value=Name(id='tax_res', ctx=Load()),
                                                                        slice=Constant(value='tag_ids', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
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
                                ),
                                Assign(
                                    targets=[Name(id='base_balance', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='tax_res', ctx=Load()),
                                        slice=Constant(value='base', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base_line_dict', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='balance', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Name(id='base_balance', ctx=Load()),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='base_balance', ctx=Load()),
                                                                        ops=[Gt()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    Name(id='base_balance', ctx=Load()),
                                                                ],
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='base_balance', ctx=Load()),
                                                                        ops=[Lt()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Name(id='base_balance', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='base_line_dict', ctx=Load()),
                                    slice=Constant(value='tax_tag_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=6, kind=None),
                                            Constant(value=0, kind=None),
                                            Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='base_tags', kind=None),
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
                        Return(
                            value=Name(id='new_aml_dicts', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_write_off_move_lines_dict',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_line', annotation=None, type_comment=None),
                            arg(arg='residual_balance', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Get move.lines dict (to be passed to the create()) corresponding to the reconciliation model's write-off lines.\n        :param st_line:             An account.bank.statement.line record.(possibly empty, if performing manual reconciliation)\n        :param residual_balance:    The residual balance of the statement line.\n        :return: A list of dict representing move.lines to be created corresponding to the write-off lines.\n        ", kind=None),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='rule_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='invoice_matching', kind=None)],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='allow_payment_tolerance',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='payment_tolerance_param',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='st_line', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='comp_curr', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='st_line', ctx=Load()),
                                        attr='company_currency_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='matched_candidates_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_matched_candidates_data',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='st_line', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='st_line_residual', ctx=Store())],
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='matched_candidates_values', ctx=Load()),
                                            slice=Constant(value='balance_sign', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Subscript(
                                            value=Name(id='matched_candidates_values', ctx=Load()),
                                            slice=Constant(value='residual_balance', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='comp_curr', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='amount_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='percentage_st_line', kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='line_ids',
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
                                    body=[
                                        Return(
                                            value=List(elts=[], ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='lines_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='amount_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='percentage', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='balance', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='comp_curr', ctx=Load()),
                                                    attr='round',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='residual_balance', ctx=Load()),
                                                        op=Mult(),
                                                        right=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='amount',
                                                                ctx=Load(),
                                                            ),
                                                            op=Div(),
                                                            right=Constant(value=100.0, kind=None),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='amount_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='percentage_st_line', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='st_line', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='balance', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='comp_curr', ctx=Load()),
                                                                    attr='round',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='st_line_residual', ctx=Load()),
                                                                        op=Mult(),
                                                                        right=BinOp(
                                                                            left=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='amount',
                                                                                ctx=Load(),
                                                                            ),
                                                                            op=Div(),
                                                                            right=Constant(value=100.0, kind=None),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='balance', ctx=Store())],
                                                            value=Constant(value=0.0, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='amount_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='regex', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='match', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='re', ctx=Load()),
                                                                    attr='search',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='amount_string',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='st_line', ctx=Load()),
                                                                        attr='payment_ref',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='match', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='sign', ctx=Store())],
                                                                    value=IfExp(
                                                                        test=Compare(
                                                                            left=Name(id='residual_balance', ctx=Load()),
                                                                            ops=[Gt()],
                                                                            comparators=[Constant(value=0.0, kind=None)],
                                                                        ),
                                                                        body=Constant(value=1, kind=None),
                                                                        orelse=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Constant(value=1, kind=None),
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Try(
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='extracted_balance', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='float', ctx=Load()),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='re', ctx=Load()),
                                                                                                    attr='sub',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    BinOp(
                                                                                                        left=Constant(value='\\D', kind=None),
                                                                                                        op=Add(),
                                                                                                        right=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='decimal_separator',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                    Constant(value='', kind=None),
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='match', ctx=Load()),
                                                                                                            attr='group',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[Constant(value=1, kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            attr='replace',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='decimal_separator',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value='.', kind=None),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='balance', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='copysign', ctx=Load()),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Name(id='extracted_balance', ctx=Load()),
                                                                                        op=Mult(),
                                                                                        right=Name(id='sign', ctx=Load()),
                                                                                    ),
                                                                                    Name(id='residual_balance', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    handlers=[
                                                                        ExceptHandler(
                                                                            type=Name(id='ValueError', ctx=Load()),
                                                                            name=None,
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='balance', ctx=Store())],
                                                                                    value=Constant(value=0, kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    finalbody=[],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='balance', ctx=Store())],
                                                                    value=Constant(value=0, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='amount_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='fixed', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='balance', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='comp_curr', ctx=Load()),
                                                                            attr='round',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='amount',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Mult(),
                                                                                right=IfExp(
                                                                                    test=Compare(
                                                                                        left=Name(id='residual_balance', ctx=Load()),
                                                                                        ops=[Gt()],
                                                                                        comparators=[Constant(value=0.0, kind=None)],
                                                                                    ),
                                                                                    body=Constant(value=1, kind=None),
                                                                                    orelse=UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Constant(value=1, kind=None),
                                                                                    ),
                                                                                ),
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
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='comp_curr', ctx=Load()),
                                            attr='is_zero',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='balance', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='writeoff_line', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='balance', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                            Constant(value='account_id', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='analytic_account_id', kind=None),
                                            Constant(value='analytic_tag_ids', kind=None),
                                            Constant(value='reconcile_model_id', kind=None),
                                        ],
                                        values=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='label',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='st_line', ctx=Load()),
                                                        attr='payment_ref',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Name(id='balance', ctx=Load()),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='balance', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            Name(id='balance', ctx=Load()),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='balance', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Name(id='balance', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='comp_curr', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='analytic_account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='analytic_tag_ids',
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
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines_vals_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='writeoff_line', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='residual_balance', ctx=Store()),
                                    op=Sub(),
                                    value=Name(id='balance', ctx=Load()),
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='tax_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='taxes', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='tax_ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='detected_fiscal_position', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.fiscal.position', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_fiscal_position',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='partner_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='detected_fiscal_position', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='taxes', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='detected_fiscal_position', ctx=Load()),
                                                            attr='map_tax',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='taxes', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='writeoff_line', ctx=Load()),
                                                    slice=Constant(value='tax_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='taxes', ctx=Load()),
                                                                attr='ids',
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
                                        If(
                                            test=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='force_tax_included',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='taxes', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='taxes', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='force_price_include',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='tax_vals_list', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_taxes_move_lines_dict',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='taxes', ctx=Load()),
                                                    Name(id='writeoff_line', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='lines_vals_list', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='tax_vals_list', ctx=Load()),
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='force_tax_included',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='tax_line', ctx=Store()),
                                                    iter=Name(id='tax_vals_list', ctx=Load()),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='residual_balance', ctx=Store()),
                                                            op=Sub(),
                                                            value=Subscript(
                                                                value=Name(id='tax_line', ctx=Load()),
                                                                slice=Constant(value='balance', kind=None),
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='lines_vals_list', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_apply_rules',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_lines', annotation=None, type_comment=None),
                            arg(arg='excluded_ids', annotation=None, type_comment=None),
                            arg(arg='partner_map', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Apply criteria to get candidates for all reconciliation models.\n\n        This function is called in enterprise by the reconciliation widget to match\n        the statement lines with the available candidates (using the reconciliation models).\n\n        :param st_lines:        Account.bank.statement.lines recordset.\n        :param excluded_ids:    Account.move.lines to exclude.\n        :param partner_map:     Dict mapping each line with new partner eventually.\n        :return:                A dict mapping each statement line id with:\n            * aml_ids:      A list of account.move.line ids.\n            * model:        An account.reconcile.model record (optional).\n            * status:       'reconciled' if the lines has been already reconciled, 'write_off' if the write-off must be\n                            applied on the statement line.\n        ", kind=None),
                        ),
                        For(
                            target=Name(id='model_name', ctx=Store()),
                            iter=Tuple(
                                elts=[
                                    Constant(value='account.bank.statement', kind=None),
                                    Constant(value='account.bank.statement.line', kind=None),
                                    Constant(value='account.move', kind=None),
                                    Constant(value='account.move.line', kind=None),
                                    Constant(value='res.company', kind=None),
                                    Constant(value='account.journal', kind=None),
                                    Constant(value='account.account', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='model_name', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='model_name', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='_fields',
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
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='line', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Dict(
                                    keys=[Constant(value='aml_ids', kind=None)],
                                    values=[List(elts=[], ctx=Load())],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='line', ctx=Store()),
                                        iter=Name(id='st_lines', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='available_models', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='rule_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='writeoff_button', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='aml_ids_to_exclude', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reconciled_amls_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines_with_partner_per_model', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=List(elts=[], ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='st_line', ctx=Store()),
                            iter=Name(id='st_lines', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='st_line', ctx=Load()),
                                            attr='amount_residual',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='mapped_partner', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='partner_map', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='partner_map', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='st_line', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.partner', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='partner_map', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='st_line', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='st_line', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='rec_model', ctx=Store()),
                                    iter=Name(id='available_models', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partner', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='mapped_partner', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='rec_model', ctx=Load()),
                                                            attr='_get_partner_from_mapping',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='st_line', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='rec_model', ctx=Load()),
                                                    attr='_is_applicable_for',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='st_line', ctx=Load()),
                                                    Name(id='partner', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='lines_with_partner_per_model', ctx=Load()),
                                                                slice=Name(id='rec_model', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='st_line', ctx=Load()),
                                                                    Name(id='partner', ctx=Load()),
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
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='matched_lines', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.bank.statement.line', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rec_model', ctx=Store()),
                            iter=Name(id='available_models', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='filtered_st_lines_with_partner', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='x', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='lines_with_partner_per_model', ctx=Load()),
                                                    slice=Name(id='rec_model', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='x', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='matched_lines', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='filtered_st_lines_with_partner', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='all_model_candidates', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec_model', ctx=Load()),
                                            attr='_get_candidates',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='filtered_st_lines_with_partner', ctx=Load()),
                                            Name(id='excluded_ids', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='st_line', ctx=Store()),
                                            Name(id='partner', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='filtered_st_lines_with_partner', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='candidates', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='all_model_candidates', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='st_line', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='candidates', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='model_rslt', ctx=Store()),
                                                                Name(id='new_reconciled_aml_ids', ctx=Store()),
                                                                Name(id='new_treated_aml_ids', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='rec_model', ctx=Load()),
                                                            attr='_get_rule_result',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='st_line', ctx=Load()),
                                                            Name(id='candidates', ctx=Load()),
                                                            Name(id='aml_ids_to_exclude', ctx=Load()),
                                                            Name(id='reconciled_amls_ids', ctx=Load()),
                                                            Name(id='partner', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='model_rslt', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='model_rslt', ctx=Load()),
                                                                    slice=Constant(value='partner', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='partner', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='results', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='st_line', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='model_rslt', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='reconciled_amls_ids', ctx=Store()),
                                                            op=BitOr(),
                                                            value=Name(id='new_reconciled_aml_ids', ctx=Load()),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='aml_ids_to_exclude', ctx=Store()),
                                                            op=BitOr(),
                                                            value=Name(id='new_treated_aml_ids', ctx=Load()),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='matched_lines', ctx=Store()),
                                                            op=Add(),
                                                            value=Name(id='st_line', ctx=Load()),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_applicable_for',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_line', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns true iff this reconciliation model can be used to search for matches\n        for the provided statement line and partner.\n        ', kind=None),
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='match_journal_ids',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='st_line', ctx=Load()),
                                                        attr='move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='journal_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='match_journal_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='match_nature',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='amount_received', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='st_line', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Lt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='match_nature',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='amount_paid', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='st_line', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='match_amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='lower', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='abs', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='st_line', ctx=Load()),
                                                            attr='amount',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[GtE()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='match_amount_max',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='match_amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='greater', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='abs', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='st_line', ctx=Load()),
                                                            attr='amount',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[LtE()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='match_amount_min',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='match_amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='between', kind=None)],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='abs', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='st_line', ctx=Load()),
                                                                    attr='amount',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='match_amount_max',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='abs', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='st_line', ctx=Load()),
                                                                    attr='amount',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Lt()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='match_amount_min',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='match_partner',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='partner', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='match_partner',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='match_partner_ids',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id='partner', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='match_partner_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='match_partner',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='match_partner_category_ids',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='category_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='match_partner_category_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='record', ctx=Store()),
                                    Name(id='rule_field', ctx=Store()),
                                    Name(id='record_field', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Name(id='st_line', ctx=Load()),
                                            Constant(value='label', kind=None),
                                            Constant(value='payment_ref', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='st_line', ctx=Load()),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='note', kind=None),
                                            Constant(value='narration', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Name(id='st_line', ctx=Load()),
                                            Constant(value='transaction_type', kind=None),
                                            Constant(value='transaction_type', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rule_term', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='self', ctx=Load()),
                                                        slice=BinOp(
                                                            left=BinOp(
                                                                left=Constant(value='match_', kind=None),
                                                                op=Add(),
                                                                right=Name(id='rule_field', ctx=Load()),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value='_param', kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='record_term', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=Name(id='record_field', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='self', ctx=Load()),
                                                            slice=BinOp(
                                                                left=Constant(value='match_', kind=None),
                                                                op=Add(),
                                                                right=Name(id='rule_field', ctx=Load()),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='contains', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='rule_term', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='record_term', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='self', ctx=Load()),
                                                            slice=BinOp(
                                                                left=Constant(value='match_', kind=None),
                                                                op=Add(),
                                                                right=Name(id='rule_field', ctx=Load()),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='not_contains', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='rule_term', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='record_term', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='self', ctx=Load()),
                                                            slice=BinOp(
                                                                left=Constant(value='match_', kind=None),
                                                                op=Add(),
                                                                right=Name(id='rule_field', ctx=Load()),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='match_regex', kind=None)],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='re', ctx=Load()),
                                                                attr='match',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='rule_term', ctx=Load()),
                                                                Name(id='record_term', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_candidates',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_lines_with_partner', annotation=None, type_comment=None),
                            arg(arg='excluded_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns the match candidates for this rule, with respect to the provided parameters.\n\n        :param st_lines_with_partner: A list of tuples (statement_line, partner),\n                                      associating each statement line to treate with\n                                      the corresponding partner, given by the partner map\n        :param excluded_ids: a set containing the ids of the amls to ignore during the search\n                             (because they already been matched by another rule)\n        ', kind=None),
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
                            targets=[Name(id='treatment_map', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='invoice_matching', kind=None),
                                    Constant(value='writeoff_suggestion', kind=None),
                                ],
                                values=[
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
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='_get_invoice_matching_query',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='st_lines_with_partner', ctx=Load()),
                                                Name(id='excluded_ids', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
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
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='_get_writeoff_suggestion_query',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='st_lines_with_partner', ctx=Load()),
                                                Name(id='excluded_ids', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query_generator', ctx=Store())],
                            value=Subscript(
                                value=Name(id='treatment_map', ctx=Load()),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rule_type',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='query', ctx=Store()),
                                        Name(id='params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='query_generator', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
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
                                    Name(id='params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rslt', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=List(elts=[], ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='candidate_dict', ctx=Store()),
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
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='rslt', ctx=Load()),
                                                slice=Subscript(
                                                    value=Name(id='candidate_dict', ctx=Load()),
                                                    slice=Constant(value='id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='candidate_dict', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='rslt', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_invoice_matching_query',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_lines_with_partner', annotation=None, type_comment=None),
                            arg(arg='excluded_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns the query applying the current invoice_matching reconciliation\n        model to the provided statement lines.\n\n        :param st_lines_with_partner: A list of tuples (statement_line, partner),\n                                      associating each statement line to treate with\n                                      the corresponding partner, given by the partner map\n        :param excluded_ids:    Account.move.lines to exclude.\n        :return:                (query, params)\n        ', kind=None),
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rule_type',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='invoice_matching', kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="Programmation Error: Can't call _get_invoice_matching_query() for different rules than 'invoice_matching'", kind=None)],
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
                            targets=[Name(id='unaccent', ctx=Store())],
                            value=Call(
                                func=Name(id='get_unaccent_wrapper', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=BinOp(
                                            left=Constant(value='\n        SELECT\n            st_line.id                          AS id,\n            aml.id                              AS aml_id,\n            aml.currency_id                     AS aml_currency_id,\n            aml.date_maturity                   AS aml_date_maturity,\n            aml.amount_residual                 AS aml_amount_residual,\n            aml.amount_residual_currency        AS aml_amount_residual_currency,\n            ', kind=None),
                                            op=Add(),
                                            right=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_select_communication_flag',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Constant(value=' AS communication_flag,\n            ', kind=None),
                                    ),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_select_payment_reference_flag',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=" AS payment_reference_flag\n        FROM account_bank_statement_line st_line\n        JOIN account_move st_line_move          ON st_line_move.id = st_line.move_id\n        JOIN res_company company                ON company.id = st_line_move.company_id\n        , account_move_line aml\n        LEFT JOIN account_move move             ON move.id = aml.move_id AND move.state = 'posted'\n        LEFT JOIN account_account account       ON account.id = aml.account_id\n        LEFT JOIN res_partner aml_partner       ON aml.partner_id = aml_partner.id\n        LEFT JOIN account_payment payment       ON payment.move_id = move.id\n        WHERE\n            aml.company_id = st_line_move.company_id\n            AND move.state = 'posted'\n            AND account.reconcile IS TRUE\n            AND aml.reconciled IS FALSE\n        ", kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='st_lines_queries', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='st_line', ctx=Store()),
                                    Name(id='partner', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='st_lines_with_partner', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='st_line', ctx=Load()),
                                            attr='amount',
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='st_line_subquery', ctx=Store())],
                                            value=Constant(value='aml.balance > 0', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='st_line_subquery', ctx=Store())],
                                            value=Constant(value='aml.balance < 0', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='match_same_currency',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='st_line_subquery', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value=' AND COALESCE(aml.currency_id, company.currency_id) = %s', kind=None),
                                                op=Mod(),
                                                right=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='st_line', ctx=Load()),
                                                                attr='foreign_currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='st_line', ctx=Load()),
                                                                    attr='move_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='partner', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='st_line_subquery', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value=' AND aml.partner_id = %s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Name(id='st_line_subquery', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=BinOp(
                                                                            left=Constant(value="\n                    AND\n                    (\n                        substring(REGEXP_REPLACE(st_line.payment_ref, '[^0-9\\s]', '', 'g'), '\\S(?:.*\\S)*') != ''\n                        AND\n                        (\n                            (", kind=None),
                                                                            op=Add(),
                                                                            right=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_get_select_communication_flag',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=')\n                            OR\n                            (', kind=None),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_get_select_payment_reference_flag',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value=")\n                        )\n                    )\n                    OR\n                    (\n                        /* We also match statement lines without partners with amls\n                        whose partner's name's parts (splitting on space) are all present\n                        within the payment_ref, in any order, with any characters between them. */\n\n                        aml_partner.name IS NOT NULL\n                        AND ", kind=None),
                                                            ),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Name(id='unaccent', ctx=Load()),
                                                                args=[Constant(value='st_line.payment_ref', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value=" ~* ('^' || (\n                            SELECT string_agg(concat('(?=.*\\m', chunk[1], '\\M)'), '')\n                              FROM regexp_matches(", kind=None),
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='unaccent', ctx=Load()),
                                                        args=[Constant(value='aml_partner.name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value=", '\\w{3,}', 'g') AS chunk\n                        ))\n                    )\n                ", kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='st_lines_queries', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='st_line.id = %s AND (%s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='st_line', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='st_line_subquery', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='query', ctx=Store()),
                            op=Add(),
                            value=BinOp(
                                left=Constant(value=' AND (%s) ', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Constant(value=' OR ', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='st_lines_queries', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='past_months_limit',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='date_limit', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
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
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='relativedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='months',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='past_months_limit',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='AND aml.date >= %(aml_date_limit)s', kind=None),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='aml_date_limit', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='date_limit', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='excluded_ids', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='AND aml.id NOT IN %(excluded_aml_ids)s', kind=None),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='excluded_aml_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[Name(id='excluded_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='matching_order',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='new_first', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=' ORDER BY aml_date_maturity DESC, aml_id DESC', kind=None),
                                ),
                            ],
                            orelse=[
                                AugAssign(
                                    target=Name(id='query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=' ORDER BY aml_date_maturity ASC, aml_id ASC', kind=None),
                                ),
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='query', ctx=Load()),
                                    Name(id='params', ctx=Load()),
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
                    name='_get_select_communication_flag',
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
                            targets=[Name(id='st_ref_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='match_text_location_label',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='st_ref_list', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[Constant(value='st_line.payment_ref', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='match_text_location_note',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='st_ref_list', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[Constant(value='st_line_move.narration', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='match_text_location_reference',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='st_ref_list', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[Constant(value='st_line_move.ref', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='st_ref', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=" || ' ' || ", kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=BinOp(
                                            left=Constant(value="COALESCE(%s, '')", kind=None),
                                            op=Mod(),
                                            right=Name(id='st_ref_name', ctx=Load()),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='st_ref_name', ctx=Store()),
                                                iter=Name(id='st_ref_list', ctx=Load()),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='st_ref', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='FALSE', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='statement_compare', ctx=Store())],
                            value=Constant(value="(\n                {move_field} IS NOT NULL AND substring(REGEXP_REPLACE({move_field}, '[^0-9\\s]', '', 'g'), '\\S(?:.*\\S)*') != ''\n                AND (\n                    regexp_split_to_array(substring(REGEXP_REPLACE({move_field}, '[^0-9\\s]', '', 'g'), '\\S(?:.*\\S)*'),'\\s+')\n                    && regexp_split_to_array(substring(REGEXP_REPLACE({st_ref}, '[^0-9\\s]', '', 'g'), '\\S(?:.*\\S)*'), '\\s+')\n                )\n            )", kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' OR ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='statement_compare', ctx=Load()),
                                                attr='format',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='move_field',
                                                    value=Name(id='field', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='st_ref',
                                                    value=Name(id='st_ref', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field', ctx=Store()),
                                                iter=List(
                                                    elts=[
                                                        Constant(value='aml.name', kind=None),
                                                        Constant(value='move.name', kind=None),
                                                        Constant(value='move.ref', kind=None),
                                                    ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_select_payment_reference_flag',
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
                            targets=[Name(id='st_ref_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='match_text_location_label',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='st_ref_list', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[Constant(value='st_line.payment_ref', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='match_text_location_note',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='st_ref_list', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[Constant(value='st_line_move.narration', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='match_text_location_reference',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='st_ref_list', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[Constant(value='st_line_move.ref', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='st_ref_list', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='FALSE', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='((move.payment_reference IS NOT NULL OR (payment.id IS NOT NULL AND move.ref IS NOT NULL)) AND ({}))', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=' OR ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=JoinedStr(
                                                    values=[
                                                        Constant(value="regexp_replace(CASE WHEN payment.id IS NULL THEN move.payment_reference ELSE move.ref END, '\\s+', '', 'g') = regexp_replace(", kind=None),
                                                        FormattedValue(
                                                            value=Name(id='st_ref', ctx=Load()),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                        Constant(value=", '\\s+', '', 'g')", kind=None),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='st_ref', ctx=Store()),
                                                        iter=Name(id='st_ref_list', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
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
                FunctionDef(
                    name='_get_partner_from_mapping',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_line', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Find partner with mapping defined on model.\n\n        For invoice matching rules, matches the statement line against each\n        regex defined in partner mapping, and returns the partner corresponding\n        to the first one matching.\n\n        :param st_line (Model<account.bank.statement.line>):\n            The statement line that needs a partner to be found\n        :return Model<res.partner>:\n            The partner found from the mapping. Can be empty an empty recordset\n            if there was nothing found from the mapping or if the function is\n            not applicable.\n        ', kind=None),
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rule_type',
                                    ctx=Load(),
                                ),
                                ops=[NotIn()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='invoice_matching', kind=None),
                                            Constant(value='writeoff_suggestion', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='partner_mapping', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner_mapping_line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='match_payment_ref', ctx=Store())],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='partner_mapping', ctx=Load()),
                                            attr='payment_ref_regex',
                                            ctx=Load(),
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='re', ctx=Load()),
                                                attr='match',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='partner_mapping', ctx=Load()),
                                                    attr='payment_ref_regex',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='st_line', ctx=Load()),
                                                    attr='payment_ref',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=True, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='match_narration', ctx=Store())],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='partner_mapping', ctx=Load()),
                                            attr='narration_regex',
                                            ctx=Load(),
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='re', ctx=Load()),
                                                attr='match',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='partner_mapping', ctx=Load()),
                                                    attr='narration_regex',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='html2text', ctx=Load()),
                                                                attr='html2text',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='st_line', ctx=Load()),
                                                                            attr='narration',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value='', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='rstrip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=True, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='match_payment_ref', ctx=Load()),
                                            Name(id='match_narration', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Name(id='partner_mapping', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_writeoff_suggestion_query',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_lines_with_partner', annotation=None, type_comment=None),
                            arg(arg='excluded_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns the query applying the current writeoff_suggestion reconciliation\n        model to the provided statement lines.\n\n        :param st_lines_with_partner: A list of tuples (statement_line, partner),\n                                      associating each statement line to treate with\n                                      the corresponding partner, given by the partner map\n        :param excluded_ids:    Account.move.lines to exclude.\n        :return:                (query, params)\n        ', kind=None),
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rule_type',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='writeoff_suggestion', kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="Programmation Error: Can't call _get_writeoff_suggestion_query() for different rules than 'writeoff_suggestion'", kind=None)],
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
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value='\n            SELECT\n                st_line.id                          AS id\n            FROM account_bank_statement_line st_line\n            WHERE st_line.id IN %(st_line_ids)s\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='st_line_ids', kind=None)],
                                values=[
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='st_line', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='st_line', ctx=Store()),
                                                                Name(id='partner', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Name(id='st_lines_with_partner', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='query', ctx=Load()),
                                    Name(id='params', ctx=Load()),
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
                    name='_get_rule_result',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_line', annotation=None, type_comment=None),
                            arg(arg='candidates', annotation=None, type_comment=None),
                            arg(arg='aml_ids_to_exclude', annotation=None, type_comment=None),
                            arg(arg='reconciled_amls_ids', annotation=None, type_comment=None),
                            arg(arg='partner_map', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get the result of a rule from the list of available candidates, depending on the\n        other reconciliations performed by previous rules.\n        ', kind=None),
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rule_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='invoice_matching', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_invoice_matching_rule_result',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='st_line', ctx=Load()),
                                            Name(id='candidates', ctx=Load()),
                                            Name(id='aml_ids_to_exclude', ctx=Load()),
                                            Name(id='reconciled_amls_ids', ctx=Load()),
                                            Name(id='partner_map', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='rule_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='writeoff_suggestion', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_writeoff_suggestion_rule_result',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='st_line', ctx=Load()),
                                                            Name(id='partner_map', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_invoice_matching_rule_result',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_line', annotation=None, type_comment=None),
                            arg(arg='candidates', annotation=None, type_comment=None),
                            arg(arg='aml_ids_to_exclude', annotation=None, type_comment=None),
                            arg(arg='reconciled_amls_ids', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='new_reconciled_aml_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_treated_aml_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='candidates', ctx=Store()),
                                        Name(id='priorities', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_filter_candidates',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='candidates', ctx=Load()),
                                    Name(id='aml_ids_to_exclude', ctx=Load()),
                                    Name(id='reconciled_amls_ids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='st_line_currency', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='st_line', ctx=Load()),
                                        attr='foreign_currency_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='st_line', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='candidate_currencies', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='candidate', ctx=Load()),
                                            slice=Constant(value='aml_currency_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='candidate', ctx=Store()),
                                                iter=Name(id='candidates', ctx=Load()),
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
                            targets=[Name(id='kept_candidates', ctx=Store())],
                            value=Name(id='candidates', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='candidate_currencies', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Set(
                                        elts=[
                                            Attribute(
                                                value=Name(id='st_line_currency', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='kept_candidates', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sum_kept_candidates', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='candidate', ctx=Store()),
                                    iter=Name(id='candidates', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='candidate_residual', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='candidate', ctx=Load()),
                                                slice=Constant(value='aml_amount_residual_currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='st_line_currency', ctx=Load()),
                                                        attr='compare_amounts',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='candidate_residual', ctx=Load()),
                                                        UnaryOp(
                                                            op=USub(),
                                                            operand=Attribute(
                                                                value=Name(id='st_line', ctx=Load()),
                                                                attr='amount_residual',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='kept_candidates', ctx=Store())],
                                                    value=List(
                                                        elts=[Name(id='candidate', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Break(),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='st_line_currency', ctx=Load()),
                                                                attr='compare_amounts',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='abs', ctx=Load()),
                                                                    args=[Name(id='sum_kept_candidates', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Name(id='abs', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='st_line', ctx=Load()),
                                                                            attr='amount_residual',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Lt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='kept_candidates', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='candidate', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='sum_kept_candidates', ctx=Store()),
                                                            op=Add(),
                                                            value=Name(id='candidate_residual', ctx=Load()),
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
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='kept_candidates_by_priority', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sort_reconciliation_candidates_by_priority',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='kept_candidates', ctx=Load()),
                                    Name(id='aml_ids_to_exclude', ctx=Load()),
                                    Name(id='reconciled_amls_ids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='priorities', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kept_candidates_by_priority', ctx=Load()),
                                            attr='keys',
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
                            targets=[Name(id='matched_candidates_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_process_matched_candidates_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='st_line', ctx=Load()),
                                    Name(id='kept_candidates', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_rule_propositions',
                                    ctx=Load(),
                                ),
                                args=[Name(id='matched_candidates_values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='rejected', kind=None),
                                ops=[In()],
                                comparators=[Name(id='status', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rslt', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='rslt', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='model', kind=None),
                                            Constant(value='aml_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='self', ctx=Load()),
                                            ListComp(
                                                elt=Subscript(
                                                    value=Name(id='candidate', ctx=Load()),
                                                    slice=Constant(value='aml_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='candidate', ctx=Store()),
                                                        iter=Name(id='kept_candidates', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_treated_aml_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='rslt', ctx=Load()),
                                                slice=Constant(value='aml_ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='allow_write_off', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='status', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='residual_balance_after_rec', ctx=Store())],
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Name(id='matched_candidates_values', ctx=Load()),
                                                    slice=Constant(value='residual_balance', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='matched_candidates_values', ctx=Load()),
                                                    slice=Constant(value='candidates_balance', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='writeoff_vals_list', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_write_off_move_lines_dict',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='st_line', ctx=Load()),
                                                    BinOp(
                                                        left=Subscript(
                                                            value=Name(id='matched_candidates_values', ctx=Load()),
                                                            slice=Constant(value='balance_sign', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        op=Mult(),
                                                        right=Name(id='residual_balance_after_rec', ctx=Load()),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='writeoff_vals_list', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='rslt', ctx=Load()),
                                                            slice=Constant(value='status', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='write_off', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='rslt', ctx=Load()),
                                                            slice=Constant(value='write_off_vals', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='writeoff_vals_list', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='writeoff_vals_list', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='allow_auto_reconcile', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='status', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='aml_ids', ctx=Store())],
                                            value=ListComp(
                                                elt=Subscript(
                                                    value=Name(id='candidate', ctx=Load()),
                                                    slice=Constant(value='aml_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='candidate', ctx=Store()),
                                                        iter=Name(id='kept_candidates', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='lines_vals_list', ctx=Store())],
                                            value=ListComp(
                                                elt=Dict(
                                                    keys=[Constant(value='id', kind=None)],
                                                    values=[Name(id='aml_id', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='aml_id', ctx=Store()),
                                                        iter=Name(id='aml_ids', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='lines_vals_list', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='priorities', ctx=Load()),
                                                        op=BitAnd(),
                                                        right=Set(
                                                            elts=[
                                                                Constant(value=1, kind=None),
                                                                Constant(value=3, kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='auto_reconcile',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='dummy', ctx=Store()),
                                                                Name(id='open_balance_vals', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='st_line', ctx=Load()),
                                                            attr='_prepare_reconciliation',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='lines_vals_list', ctx=Load()),
                                                                op=Add(),
                                                                right=Name(id='writeoff_vals_list', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='open_balance_vals', ctx=Load()),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='open_balance_vals', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='account_id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=Attribute(
                                                                            value=Name(id='st_line', ctx=Load()),
                                                                            attr='partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Name(id='partner', ctx=Load()),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='st_line', ctx=Load()),
                                                                            attr='partner_id',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='st_line', ctx=Load()),
                                                                    attr='reconcile',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='lines_vals_list', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Name(id='writeoff_vals_list', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='allow_partial',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='rslt', ctx=Load()),
                                                                    slice=Constant(value='status', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='reconciled', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='rslt', ctx=Load()),
                                                                    slice=Constant(value='reconciled_lines', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Attribute(
                                                                value=Name(id='st_line', ctx=Load()),
                                                                attr='line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='new_reconciled_aml_ids', ctx=Store())],
                                                            value=Name(id='new_treated_aml_ids', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='rslt', ctx=Load()),
                                    Name(id='new_reconciled_aml_ids', ctx=Load()),
                                    Name(id='new_treated_aml_ids', ctx=Load()),
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
                    name='_process_matched_candidates_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='statement_line', annotation=None, type_comment=None),
                            arg(arg='candidates', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Simulate the reconciliation of the statement line with the candidates and\n        compute some useful data to perform all the matching rules logic.\n\n        :param statement_line:  An account.bank.statement.line record.\n        :param candidates:      Fetched account.move.lines from query (dict).\n        :return:                A python dict containing:\n            * currency:                 The currency of the transaction.\n            * statement_line:           The statement line matching the candidates.\n            * candidates:               Fetched account.move.lines from query (dict).\n            * reconciliation_overview:  The computed reconciliation from '_prepare_reconciliation'.\n            * open_balance_vals:        The open balance returned by '_prepare_reconciliation'.\n            * balance_sign:             The sign applied to the balance to make amounts always positive.\n            * residual_balance:         The residual balance of the statement line before reconciling anything,\n                                        always positive and expressed in company's currency.\n            * candidates_balance:       The balance of candidates lines expressed in company's currency.\n            * residual_balance_curr:    The residual balance of the statement line before reconciling anything,\n                                        always positive and expressed in transaction's currency.\n            * candidates_balance_curr:  The balance of candidates lines expressed in transaction's currency.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='candidates', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='candidates', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='reconciliation_overview', ctx=Store()),
                                        Name(id='open_balance_vals', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='statement_line', ctx=Load()),
                                    attr='_prepare_reconciliation',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='currency_id', kind=None),
                                                Constant(value='amount_residual', kind=None),
                                                Constant(value='amount_residual_currency', kind=None),
                                            ],
                                            values=[
                                                Subscript(
                                                    value=Name(id='aml', ctx=Load()),
                                                    slice=Constant(value='aml_currency_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='aml', ctx=Load()),
                                                    slice=Constant(value='aml_amount_residual', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='aml', ctx=Load()),
                                                    slice=Constant(value='aml_amount_residual_currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='aml', ctx=Store()),
                                                iter=Name(id='candidates', ctx=Load()),
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
                                Tuple(
                                    elts=[
                                        Name(id='liquidity_lines', ctx=Store()),
                                        Name(id='suspense_lines', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='statement_line', ctx=Load()),
                                    attr='_seek_for_lines',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='statement_line', ctx=Load()),
                                attr='to_check',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='stl_residual_balance', ctx=Store())],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Attribute(
                                            value=Name(id='liquidity_lines', ctx=Load()),
                                            attr='balance',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='stl_residual_balance_curr', ctx=Store())],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Attribute(
                                            value=Name(id='liquidity_lines', ctx=Load()),
                                            attr='amount_currency',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='suspense_lines', ctx=Load()),
                                            attr='account_id',
                                            ctx=Load(),
                                        ),
                                        attr='reconcile',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='stl_residual_balance', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='suspense_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='amount_residual', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='stl_residual_balance_curr', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='suspense_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='amount_residual_currency', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='stl_residual_balance', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='suspense_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='balance', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='stl_residual_balance_curr', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='suspense_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='amount_currency', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='candidates_balance', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='candidates_balance_curr', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='reconciliation_vals', ctx=Store()),
                            iter=Name(id='reconciliation_overview', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='line_vals', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='reconciliation_vals', ctx=Load()),
                                        slice=Constant(value='line_vals', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='candidates_balance', ctx=Store()),
                                    op=Sub(),
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='line_vals', ctx=Load()),
                                            slice=Constant(value='debit', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Subscript(
                                            value=Name(id='line_vals', ctx=Load()),
                                            slice=Constant(value='credit', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='line_vals', ctx=Load()),
                                        slice=Constant(value='currency_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='candidates_balance_curr', ctx=Store()),
                                            op=Sub(),
                                            value=Subscript(
                                                value=Name(id='line_vals', ctx=Load()),
                                                slice=Constant(value='amount_currency', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Name(id='candidates_balance_curr', ctx=Store()),
                                            op=Sub(),
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Name(id='line_vals', ctx=Load()),
                                                    slice=Constant(value='debit', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Subscript(
                                                    value=Name(id='line_vals', ctx=Load()),
                                                    slice=Constant(value='credit', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='balance_sign', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='stl_residual_balance', ctx=Load()),
                                    ops=[Gt()],
                                    comparators=[Constant(value=0.0, kind=None)],
                                ),
                                body=Constant(value=1, kind=None),
                                orelse=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='currency', kind=None),
                                    Constant(value='statement_line', kind=None),
                                    Constant(value='candidates', kind=None),
                                    Constant(value='reconciliation_overview', kind=None),
                                    Constant(value='open_balance_vals', kind=None),
                                    Constant(value='balance_sign', kind=None),
                                    Constant(value='residual_balance', kind=None),
                                    Constant(value='candidates_balance', kind=None),
                                    Constant(value='residual_balance_curr', kind=None),
                                    Constant(value='candidates_balance_curr', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='statement_line', ctx=Load()),
                                                attr='foreign_currency_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='statement_line', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Name(id='statement_line', ctx=Load()),
                                    Name(id='candidates', ctx=Load()),
                                    Name(id='reconciliation_overview', ctx=Load()),
                                    Name(id='open_balance_vals', ctx=Load()),
                                    Name(id='balance_sign', ctx=Load()),
                                    BinOp(
                                        left=Name(id='balance_sign', ctx=Load()),
                                        op=Mult(),
                                        right=Name(id='stl_residual_balance', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='balance_sign', ctx=Load()),
                                        op=Mult(),
                                        right=Name(id='candidates_balance', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='balance_sign', ctx=Load()),
                                        op=Mult(),
                                        right=Name(id='stl_residual_balance_curr', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='balance_sign', ctx=Load()),
                                        op=Mult(),
                                        right=Name(id='candidates_balance_curr', ctx=Load()),
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
                    name='_check_rule_propositions',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='matched_candidates_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check restrictions that can't be handled for each move.line separately.\n        Note: Only used by models having a type equals to 'invoice_matching'.\n\n        :param matched_candidates_values: The values computed by '_process_matched_candidates_data'.\n        :return: A string representing what to do with the candidates:\n            * rejected:             Reject candidates.\n            * allow_write_off:      Allow to generate the write-off from the reconcile model lines if specified.\n            * allow_auto_reconcile: Allow to automatically reconcile entries if 'auto_validate' is enabled.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='candidates', ctx=Store())],
                            value=Subscript(
                                value=Name(id='matched_candidates_values', ctx=Load()),
                                slice=Constant(value='candidates', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Subscript(
                                value=Name(id='matched_candidates_values', ctx=Load()),
                                slice=Constant(value='currency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='allow_payment_tolerance',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Set(
                                        elts=[
                                            Constant(value='allow_write_off', kind=None),
                                            Constant(value='allow_auto_reconcile', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='candidates', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Set(
                                        elts=[Constant(value='rejected', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='residual_balance_after_rec', ctx=Store())],
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='matched_candidates_values', ctx=Load()),
                                    slice=Constant(value='residual_balance_curr', kind=None),
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='matched_candidates_values', ctx=Load()),
                                    slice=Constant(value='candidates_balance_curr', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='currency', ctx=Load()),
                                    attr='is_zero',
                                    ctx=Load(),
                                ),
                                args=[Name(id='residual_balance_after_rec', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Set(
                                        elts=[Constant(value='allow_auto_reconcile', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='residual_balance_after_rec', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=0.0, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Set(
                                        elts=[Constant(value='allow_auto_reconcile', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='payment_tolerance_param',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Set(
                                        elts=[Constant(value='rejected', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='payment_tolerance_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='fixed_amount', kind=None)],
                                    ),
                                    Compare(
                                        left=UnaryOp(
                                            op=USub(),
                                            operand=Name(id='residual_balance_after_rec', ctx=Load()),
                                        ),
                                        ops=[LtE()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='payment_tolerance_param',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Set(
                                        elts=[
                                            Constant(value='allow_write_off', kind=None),
                                            Constant(value='allow_auto_reconcile', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='reconciled_percentage_left', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='residual_balance_after_rec', ctx=Load()),
                                    op=Div(),
                                    right=Subscript(
                                        value=Name(id='matched_candidates_values', ctx=Load()),
                                        slice=Constant(value='candidates_balance_curr', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                                op=Mult(),
                                right=Constant(value=100.0, kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='payment_tolerance_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='percentage', kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='reconciled_percentage_left', ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='payment_tolerance_param',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Set(
                                        elts=[
                                            Constant(value='allow_write_off', kind=None),
                                            Constant(value='allow_auto_reconcile', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Set(
                                elts=[Constant(value='rejected', kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filter_candidates',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='candidates', annotation=None, type_comment=None),
                            arg(arg='aml_ids_to_exclude', annotation=None, type_comment=None),
                            arg(arg='reconciled_amls_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Sorts reconciliation candidates by priority and filters them so that only\n        the most prioritary are kept.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='candidates_by_priority', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sort_reconciliation_candidates_by_priority',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='candidates', ctx=Load()),
                                    Name(id='aml_ids_to_exclude', ctx=Load()),
                                    Name(id='reconciled_amls_ids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='candidates_by_priority', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            List(elts=[], ctx=Load()),
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='max_priority', ctx=Store())],
                            value=Call(
                                func=Name(id='min', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='candidates_by_priority', ctx=Load()),
                                            attr='keys',
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
                            targets=[Name(id='filtered_candidates', ctx=Store())],
                            value=Subscript(
                                value=Name(id='candidates_by_priority', ctx=Load()),
                                slice=Name(id='max_priority', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filtered_priorities', ctx=Store())],
                            value=Set(
                                elts=[Name(id='max_priority', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='max_priority', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='proposed_priority', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='max_priority', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='filtered_candidates', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Name(id='candidates_by_priority', ctx=Load()),
                                        slice=Name(id='proposed_priority', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='candidates_by_priority', ctx=Load()),
                                        slice=Name(id='proposed_priority', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='filtered_priorities', ctx=Load()),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='proposed_priority', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='filtered_candidates', ctx=Load()),
                                    Name(id='filtered_priorities', ctx=Load()),
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
                    name='_sort_reconciliation_candidates_by_priority',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='candidates', annotation=None, type_comment=None),
                            arg(arg='already_proposed_aml_ids', annotation=None, type_comment=None),
                            arg(arg='already_reconciled_aml_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Sorts the provided candidates and returns a mapping of candidates by\n        priority (1 being the highest).\n\n        The priorities are defined as follows:\n\n        1: payment_reference_flag is true,  so the move's payment_reference\n           field matches the statement line's.\n\n        2: Same as 1, but the candidates have already been proposed for a previous statement line\n\n        3: communication_flag is true, so either the move's ref, move's name or\n           aml's name match the statement line's payment reference.\n\n        4: Same as 3, but the candidates have already been proposed for a previous statement line\n\n        5: candidates proposed by the query, but no match with the statement\n           line's payment ref could be found.\n\n        6: Same as 5, but the candidates have already been proposed for a previous statement line\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='candidates_by_priority', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=List(elts=[], ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='candidate', ctx=Store()),
                            iter=Call(
                                func=Name(id='filter', ctx=Load()),
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
                                            left=Subscript(
                                                value=Name(id='x', ctx=Load()),
                                                slice=Constant(value='aml_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            ops=[NotIn()],
                                            comparators=[Name(id='already_reconciled_aml_ids', ctx=Load())],
                                        ),
                                    ),
                                    Name(id='candidates', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Subscript(
                                        value=Name(id='candidate', ctx=Load()),
                                        slice=Constant(value='payment_reference_flag', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='priority', ctx=Store())],
                                            value=Constant(value=1, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Subscript(
                                                value=Name(id='candidate', ctx=Load()),
                                                slice=Constant(value='communication_flag', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='priority', ctx=Store())],
                                                    value=Constant(value=3, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='priority', ctx=Store())],
                                                    value=Constant(value=5, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='candidate', ctx=Load()),
                                            slice=Constant(value='aml_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='already_proposed_aml_ids', ctx=Load())],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='priority', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='candidates_by_priority', ctx=Load()),
                                                slice=Name(id='priority', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='candidate', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='candidates_by_priority', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_writeoff_suggestion_rule_result',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='st_line', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='matched_candidates_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_process_matched_candidates_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='st_line', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='residual_balance_after_rec', ctx=Store())],
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='matched_candidates_values', ctx=Load()),
                                    slice=Constant(value='residual_balance', kind=None),
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='matched_candidates_values', ctx=Load()),
                                    slice=Constant(value='candidates_balance', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='writeoff_vals_list', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_write_off_move_lines_dict',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='st_line', ctx=Load()),
                                    BinOp(
                                        left=Subscript(
                                            value=Name(id='matched_candidates_values', ctx=Load()),
                                            slice=Constant(value='balance_sign', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Name(id='residual_balance_after_rec', ctx=Load()),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rslt', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='model', kind=None),
                                    Constant(value='status', kind=None),
                                    Constant(value='aml_ids', kind=None),
                                    Constant(value='write_off_vals', kind=None),
                                ],
                                values=[
                                    Name(id='self', ctx=Load()),
                                    Constant(value='write_off', kind=None),
                                    List(elts=[], ctx=Load()),
                                    Name(id='writeoff_vals_list', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='writeoff_vals_list', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='auto_reconcile',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='st_line', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Name(id='partner', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='st_line', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='partner', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='st_line', ctx=Load()),
                                            attr='reconcile',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='writeoff_vals_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rslt', ctx=Load()),
                                            slice=Constant(value='status', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='reconciled', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rslt', ctx=Load()),
                                            slice=Constant(value='reconciled_lines', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='st_line', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='rslt', ctx=Load()),
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
