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
            names=[
                alias(name='UserError', asname=None),
                alias(name='RedirectWarning', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='AccountMove',
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
                    value=Constant(value='account.move', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_l10n_ar_get_document_number_parts',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='document_number', annotation=None, type_comment=None),
                            arg(arg='document_type_code', annotation=None, type_comment=None),
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
                                left=Name(id='document_type_code', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='66', kind=None),
                                            Constant(value='67', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='pos', ctx=Store()),
                                        Name(id='invoice_number', ctx=Store()),
                                    ],
                                    value=Constant(value='0', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='pos', ctx=Store()),
                                                Name(id='invoice_number', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='document_number', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='-', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='invoice_number', kind=None),
                                    Constant(value='point_of_sale', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='invoice_number', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='pos', ctx=Load())],
                                        keywords=[],
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
                Assign(
                    targets=[Name(id='l10n_ar_afip_responsibility_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='l10n_ar.afip.responsibility.type', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='AFIP Responsibility Type', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Defined by AFIP to identify the type of responsibilities that a person or a legal entity could have and that impacts in the type of operations and requirements they need.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ar_currency_rate', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=6, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Currency Rate', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ar_afip_concept', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_ar_afip_concept', kind=None),
                            ),
                            keyword(
                                arg='selection',
                                value=Constant(value='_get_afip_invoice_concepts', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='AFIP Concept', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='A concept is suggested regarding the type of the products on the invoice but it is allowed to force a different type if required.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ar_afip_service_start', ctx=Store())],
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
                                value=Constant(value='AFIP Service Start Date', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='draft', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=False, kind=None),
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
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ar_afip_service_end', ctx=Store())],
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
                                value=Constant(value='AFIP Service End Date', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='draft', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=False, kind=None),
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
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_moves_use_documents',
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
                            value=Constant(value=' Do not let to create not invoices entries in journals that use documents ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='not_invoices', ctx=Store())],
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
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
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
                                                            value=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='account_fiscal_country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='AR', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='journal_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='sale', kind=None),
                                                                Constant(value='purchase', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                Attribute(
                                                    value=Name(id='x', ctx=Load()),
                                                    attr='l10n_latam_use_documents',
                                                    ctx=Load(),
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Call(
                                                        func=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='is_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
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
                            test=Name(id='not_invoices', ctx=Load()),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="The selected Journal can't be used in this transaction, please select one that doesn't use documents as these are just for Invoices.", kind=None)],
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
                                Constant(value='move_type', kind=None),
                                Constant(value='journal_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_invoice_type_document_type',
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
                            value=Constant(value=" LATAM module define that we are not able to use debit_note or invoice document types in an invoice refunds,\n        However for Argentinian Document Type's 99 (internal type = invoice) we are able to used in a refund invoices.\n\n        In this method we exclude the argentinian document type 99 from the generic constraint ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ar_doctype_99', ctx=Store())],
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
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
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
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='country_code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='AR', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='l10n_latam_document_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='99', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='move_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='out_refund', kind=None),
                                                                Constant(value='in_refund', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
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
                                            Name(id='AccountMove', ctx=Load()),
                                            BinOp(
                                                left=Name(id='self', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='ar_doctype_99', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_check_invoice_type_document_type',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                Constant(value='move_type', kind=None),
                                Constant(value='l10n_latam_document_type_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_afip_invoice_concepts',
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
                            value=Constant(value=' Return the list of values of the selection field. ', kind=None),
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='1', kind=None),
                                            Constant(value='Products / Definitive export of goods', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='2', kind=None),
                                            Constant(value='Services', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='3', kind=None),
                                            Constant(value='Products and Services', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='4', kind=None),
                                            Constant(value='4-Other (export)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
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
                    name='_compute_l10n_ar_afip_concept',
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
                            targets=[Name(id='recs_afip', ctx=Store())],
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
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
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
                                                            value=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='account_fiscal_country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='AR', kind=None)],
                                                ),
                                                Attribute(
                                                    value=Name(id='x', ctx=Load()),
                                                    attr='l10n_latam_use_documents',
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
                        For(
                            target=Name(id='rec', ctx=Store()),
                            iter=Name(id='recs_afip', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='l10n_ar_afip_concept',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='_get_concept',
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
                        Assign(
                            targets=[Name(id='remaining', ctx=Store())],
                            value=BinOp(
                                left=Name(id='self', ctx=Load()),
                                op=Sub(),
                                right=Name(id='recs_afip', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='remaining', ctx=Load()),
                                    attr='l10n_ar_afip_concept',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
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
                                Constant(value='invoice_line_ids', kind=None),
                                Constant(value='invoice_line_ids.product_id', kind=None),
                                Constant(value='invoice_line_ids.product_id.type', kind=None),
                                Constant(value='journal_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_concept',
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
                            value=Constant(value=' Method to get the concept of the invoice considering the type of the products on the invoice ', kind=None),
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
                            targets=[Name(id='invoice_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice_line_ids',
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
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='display_type',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_types', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Attribute(
                                            value=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='invoice_lines', ctx=Load()),
                                                ifs=[
                                                    Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                            targets=[Name(id='consumable', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='consu', kind=None),
                                            Constant(value='product', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='service', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    List(
                                        elts=[Constant(value='service', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expo_invoice', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='l10n_latam_document_type_id',
                                        ctx=Load(),
                                    ),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='19', kind=None),
                                            Constant(value='20', kind=None),
                                            Constant(value='21', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='afip_concept', ctx=Store())],
                            value=Constant(value='1', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='product_types', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='service', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='afip_concept', ctx=Store())],
                                    value=Constant(value='2', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            BinOp(
                                                left=Name(id='product_types', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='consumable', ctx=Load()),
                                            ),
                                            BinOp(
                                                left=Name(id='product_types', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='service', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='expo_invoice', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='afip_concept', ctx=Store())],
                                            value=Constant(value='3', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='afip_concept', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_l10n_latam_documents_domain',
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
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_l10n_latam_documents_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='account_fiscal_country_id',
                                        ctx=Load(),
                                    ),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='AR', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='letters', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='_get_journal_letter',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='counterpart_partner',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='commercial_partner_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='l10n_ar_letter', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='l10n_ar_letter', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='letters', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='codes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='_get_journal_codes',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='codes', ctx=Load()),
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
                                                            Constant(value='code', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='codes', ctx=Load()),
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
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='move_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='in_refund', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=BinOp(
                                                left=List(
                                                    elts=[
                                                        Constant(value='|', kind=None),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='code', kind=None),
                                                                Constant(value='in', kind=None),
                                                                List(
                                                                    elts=[Constant(value='99', kind=None)],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Name(id='domain', ctx=Load()),
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
                            value=Name(id='domain', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_argentinean_invoice_taxes',
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
                            target=Name(id='inv', ctx=Store()),
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
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_ar_company_requires_vat',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='purchase_aliquots', ctx=Store())],
                                    value=Constant(value='not_zero', kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='inv', ctx=Load()),
                                                    attr='move_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='in_invoice', kind=None),
                                                            Constant(value='in_refund', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='inv', ctx=Load()),
                                                        attr='l10n_latam_document_type_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='purchase_aliquots',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='zero', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='purchase_aliquots', ctx=Store())],
                                            value=Constant(value='zero', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='inv', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='invoice_line_ids', kind=None)],
                                                keywords=[],
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
                                                        attr='display_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotIn()],
                                                    comparators=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='line_section', kind=None),
                                                                Constant(value='line_note', kind=None),
                                                            ],
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
                                            targets=[Name(id='vat_taxes', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
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
                                                        body=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='tax_group_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='l10n_ar_vat_afip_code',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='vat_taxes', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='There must be one and only one VAT tax per line. Check line "%s"', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='name',
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
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='purchase_aliquots', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='zero', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='vat_taxes', ctx=Load()),
                                                                        attr='tax_group_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='l10n_ar_vat_afip_code',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='0', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='On invoice id "%s" you must use VAT Not Applicable on every line.', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Mod(),
                                                                        right=Attribute(
                                                                            value=Name(id='inv', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
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
                                                                        left=Name(id='purchase_aliquots', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='not_zero', kind=None)],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='vat_taxes', ctx=Load()),
                                                                                attr='tax_group_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='l10n_ar_vat_afip_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='0', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Name(id='UserError', ctx=Load()),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Call(
                                                                                    func=Name(id='_', ctx=Load()),
                                                                                    args=[Constant(value='On invoice id "%s" you must use VAT taxes different than VAT Not Applicable.', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Mod(),
                                                                                right=Attribute(
                                                                                    value=Name(id='inv', ctx=Load()),
                                                                                    attr='id',
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_afip_service_dates',
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
                            target=Name(id='rec', ctx=Store()),
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
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
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
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='invoice_date',
                                                    ctx=Load(),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='l10n_ar_afip_concept',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='2', kind=None),
                                                                Constant(value='3', kind=None),
                                                                Constant(value='4', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
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
                                            value=Name(id='rec', ctx=Load()),
                                            attr='l10n_ar_afip_service_start',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='l10n_ar_afip_service_start',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='invoice_date',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='day',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='l10n_ar_afip_service_end',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='l10n_ar_afip_service_end',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='invoice_date',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='day',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                        keyword(
                                                            arg='days',
                                                            value=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                        ),
                                                        keyword(
                                                            arg='months',
                                                            value=UnaryOp(
                                                                op=UAdd(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                        ),
                                                    ],
                                                ),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_afip_responsibility',
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='account_fiscal_country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='AR', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='l10n_latam_use_documents',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_ar_afip_responsibility_type_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='warning', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Missing Partner Configuration', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Please configure the AFIP Responsibility for "%s" in order to continue', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
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
                            args=[Constant(value='partner_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_partner_journal',
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
                            value=Constant(value=' This method is used when the invoice is created from the sale or subscription ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='expo_journals', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='FEERCEL', kind=None),
                                    Constant(value='FEEWS', kind=None),
                                    Constant(value='FEERCELP', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rec', ctx=Store()),
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
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
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
                                                            value=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='account_fiscal_country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='AR', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='journal_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='sale', kind=None)],
                                                ),
                                                Attribute(
                                                    value=Name(id='x', ctx=Load()),
                                                    attr='l10n_latam_use_documents',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='l10n_ar_afip_responsibility_type_id',
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
                                    targets=[Name(id='res_code', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_ar_afip_responsibility_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
                                                            value=Name(id='rec', ctx=Load()),
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
                                                    Constant(value='l10n_latam_use_documents', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='sale', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='journal', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.journal', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='msg', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='res_code', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='9', kind=None),
                                                            Constant(value='10', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='rec', ctx=Load()),
                                                        attr='journal_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='l10n_ar_afip_pos_system',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[Name(id='expo_journals', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='journal', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='journal', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='domain', ctx=Load()),
                                                        op=Add(),
                                                        right=List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='l10n_ar_afip_pos_system', kind=None),
                                                                        Constant(value='in', kind=None),
                                                                        Name(id='expo_journals', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
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
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="You are trying to create an invoice for foreign partner but you don't have an exportation journal", kind=None)],
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
                                                    Compare(
                                                        left=Name(id='res_code', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='9', kind=None),
                                                                    Constant(value='10', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='rec', ctx=Load()),
                                                                attr='journal_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='l10n_ar_afip_pos_system',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='expo_journals', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='journal', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='journal', ctx=Load()),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='domain', ctx=Load()),
                                                                op=Add(),
                                                                right=List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='l10n_ar_afip_pos_system', kind=None),
                                                                                Constant(value='not in', kind=None),
                                                                                Name(id='expo_journals', ctx=Load()),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
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
                                                    targets=[Name(id='msg', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="You are trying to create an invoice for domestic partner but you don't have a domestic market journal", kind=None)],
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
                                    test=Name(id='journal', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='journal_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='journal', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Name(id='msg', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='action', ctx=Store())],
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
                                                        args=[Constant(value='account.action_account_journal_form', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='RedirectWarning', ctx=Load()),
                                                        args=[
                                                            Name(id='msg', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='action', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Go to Journals', kind=None)],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
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
                    name='_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='soft', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ar_invoices', ctx=Store())],
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
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
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
                                                            value=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='account_fiscal_country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='AR', kind=None)],
                                                ),
                                                Attribute(
                                                    value=Name(id='x', ctx=Load()),
                                                    attr='l10n_latam_use_documents',
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
                        For(
                            target=Name(id='rec', ctx=Store()),
                            iter=Name(id='ar_invoices', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='l10n_ar_afip_responsibility_type_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='commercial_partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_ar_afip_responsibility_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='l10n_ar_currency_rate',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=1.0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='l10n_ar_currency_rate',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='rec', ctx=Load()),
                                                            attr='l10n_ar_currency_rate',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='rec', ctx=Load()),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_convert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=1.0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='rec', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='rec', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='rec', ctx=Load()),
                                                                        attr='invoice_date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
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
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='round',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ar_invoices', ctx=Load()),
                                    attr='_check_argentinean_invoice_taxes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='posted', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[Name(id='soft', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='posted', ctx=Load()),
                                    attr='_set_afip_service_dates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='posted', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_reverse_moves',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default_values_list', annotation=None, type_comment=None),
                            arg(arg='cancel', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='default_values_list', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='default_values_list', ctx=Store())],
                                    value=ListComp(
                                        elt=Dict(keys=[], values=[]),
                                        generators=[
                                            comprehension(
                                                target=Name(id='move', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='move', ctx=Store()),
                                    Name(id='default_values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='default_values_list', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='default_values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='l10n_ar_afip_service_start', kind=None),
                                                    Constant(value='l10n_ar_afip_service_end', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='l10n_ar_afip_service_start',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='l10n_ar_afip_service_end',
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
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default_values_list',
                                        value=Name(id='default_values_list', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='cancel',
                                        value=Name(id='cancel', ctx=Load()),
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
                    name='_inverse_l10n_latam_document_number',
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
                                    attr='_inverse_l10n_latam_document_number',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='to_review', ctx=Store())],
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
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
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
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='journal_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='sale', kind=None)],
                                                ),
                                                Attribute(
                                                    value=Name(id='x', ctx=Load()),
                                                    attr='l10n_latam_document_type_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='x', ctx=Load()),
                                                    attr='l10n_latam_document_number',
                                                    ctx=Load(),
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='l10n_latam_manual_document_number',
                                                            ctx=Load(),
                                                        ),
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='highest_name',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='l10n_latam_document_type_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='AR', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rec', ctx=Store()),
                            iter=Name(id='to_review', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='number', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='l10n_latam_document_type_id',
                                                ctx=Load(),
                                            ),
                                            attr='_format_document_number',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='l10n_latam_document_number',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='current_pos', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='number', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='-', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='current_pos', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='journal_id',
                                                    ctx=Load(),
                                                ),
                                                attr='l10n_ar_afip_pos_number',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='invoices', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='journal_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='rec', ctx=Load()),
                                                                            attr='journal_id',
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
                                                                    Constant(value='posted_before', kind=None),
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
                                                        arg='limit',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='invoices', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='rec', ctx=Load()),
                                                                attr='journal_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='l10n_ar_afip_pos_number',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='current_pos', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='rec', ctx=Load()),
                                                                attr='journal_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_onchange_set_short_name',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='The document number can not be changed for this journal, you can only modify the POS number if there is not posted (or posted before) invoices', kind=None)],
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
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='l10n_latam_document_type_id', kind=None),
                                Constant(value='l10n_latam_document_number', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_formatted_sequence',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Constant(value='%s %05d-%08d', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='l10n_latam_document_type_id',
                                                ctx=Load(),
                                            ),
                                            attr='doc_code_prefix',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_ar_afip_pos_number',
                                            ctx=Load(),
                                        ),
                                        Name(id='number', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_starting_sequence',
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
                            value=Constant(value=' If use documents then will create a new starting sequence using the document type code prefix and the\n        journal document number with a 8 padding number ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Load(),
                                        ),
                                        attr='l10n_latam_use_documents',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
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
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='AR', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='l10n_latam_document_type_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_formatted_sequence',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_starting_sequence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_last_sequence_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='relaxed', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='where_string', ctx=Store()),
                                        Name(id='param', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountMove', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_last_sequence_domain',
                                    ctx=Load(),
                                ),
                                args=[Name(id='relaxed', ctx=Load())],
                                keywords=[],
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
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='account_fiscal_country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='AR', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='l10n_latam_use_documents',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_ar_share_sequences',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='where_string', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=' AND l10n_latam_document_type_id = %(l10n_latam_document_type_id)s', kind=None),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='param', ctx=Load()),
                                                    slice=Constant(value='l10n_latam_document_type_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='l10n_latam_document_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='journal_id',
                                                    ctx=Load(),
                                                ),
                                                attr='l10n_ar_share_sequences',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='where_string', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=' AND l10n_latam_document_type_id in %(l10n_latam_document_type_ids)s', kind=None),
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='param', ctx=Load()),
                                                            slice=Constant(value='l10n_latam_document_type_ids', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='l10n_latam_document_type_id',
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
                                                                                        Constant(value='l10n_ar_letter', kind=None),
                                                                                        Constant(value='=', kind=None),
                                                                                        Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='l10n_latam_document_type_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='l10n_ar_letter',
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
                                                                attr='ids',
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
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='where_string', ctx=Load()),
                                    Name(id='param', ctx=Load()),
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
                    name='_l10n_ar_get_amounts',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company_currency', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Method used to prepare data to present amounts and taxes related amounts when creating an\n        electronic invoice for argentinean and the txt files for digital VAT books. Only take into account the argentinean taxes ', kind=None),
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
                            targets=[Name(id='amount_field', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='company_currency', ctx=Load()),
                                            Constant(value='balance', kind=None),
                                        ],
                                    ),
                                    Constant(value='price_subtotal', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sign', ctx=Store())],
                            value=IfExp(
                                test=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id='company_currency', ctx=Load()),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='is_inbound',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                ),
                                body=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                orelse=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tax_line_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vat_taxes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tax_lines', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='r', ctx=Load()),
                                                    attr='tax_line_id',
                                                    ctx=Load(),
                                                ),
                                                attr='tax_group_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_ar_vat_afip_code',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vat_taxable', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move.line', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='invoice_line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='tax', ctx=Load()),
                                                                attr='tax_group_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='l10n_ar_vat_afip_code',
                                                            ctx=Load(),
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='tax', ctx=Load()),
                                                                    attr='tax_group_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='l10n_ar_vat_afip_code',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotIn()],
                                                            comparators=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='0', kind=None),
                                                                        Constant(value='1', kind=None),
                                                                        Constant(value='2', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='tax', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='tax_ids',
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
                                        AugAssign(
                                            target=Name(id='vat_taxable', ctx=Store()),
                                            op=BitOr(),
                                            value=Name(id='line', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profits_tax_group', ctx=Store())],
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
                                args=[Constant(value='l10n_ar.tax_group_percepcion_ganancias', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='vat_amount', kind=None),
                                    Constant(value='vat_taxable_amount', kind=None),
                                    Constant(value='vat_exempt_base_amount', kind=None),
                                    Constant(value='vat_untaxed_base_amount', kind=None),
                                    Constant(value='not_vat_taxes_amount', kind=None),
                                    Constant(value='iibb_perc_amount', kind=None),
                                    Constant(value='mun_perc_amount', kind=None),
                                    Constant(value='intern_tax_amount', kind=None),
                                    Constant(value='other_taxes_amount', kind=None),
                                    Constant(value='profits_perc_amount', kind=None),
                                    Constant(value='vat_perc_amount', kind=None),
                                    Constant(value='other_perc_amount', kind=None),
                                ],
                                values=[
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='vat_taxes', ctx=Load()),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    IfExp(
                                        test=Compare(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='l10n_latam_document_type_id',
                                                    ctx=Load(),
                                                ),
                                                attr='l10n_ar_letter',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(value='C', kind=None)],
                                        ),
                                        body=BinOp(
                                            left=Name(id='sign', ctx=Load()),
                                            op=Mult(),
                                            right=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='vat_taxable', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='amount_field', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        orelse=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='amount_untaxed',
                                            ctx=Load(),
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='invoice_line_ids',
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
                                                                    body=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='x', ctx=Load()),
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
                                                                                    args=[arg(arg='y', annotation=None, type_comment=None)],
                                                                                    vararg=None,
                                                                                    kwonlyargs=[],
                                                                                    kw_defaults=[],
                                                                                    kwarg=None,
                                                                                    defaults=[],
                                                                                ),
                                                                                body=Compare(
                                                                                    left=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='y', ctx=Load()),
                                                                                            attr='tax_group_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='l10n_ar_vat_afip_code',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Constant(value='2', kind=None)],
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='invoice_line_ids',
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
                                                                    body=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='x', ctx=Load()),
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
                                                                                    args=[arg(arg='y', annotation=None, type_comment=None)],
                                                                                    vararg=None,
                                                                                    kwonlyargs=[],
                                                                                    kw_defaults=[],
                                                                                    kwarg=None,
                                                                                    defaults=[],
                                                                                ),
                                                                                body=Compare(
                                                                                    left=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='y', ctx=Load()),
                                                                                            attr='tax_group_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='l10n_ar_vat_afip_code',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Constant(value='1', kind=None)],
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=BinOp(
                                                            left=Name(id='tax_lines', ctx=Load()),
                                                            op=Sub(),
                                                            right=Name(id='vat_taxes', ctx=Load()),
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='tax_lines', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='r', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='r', ctx=Load()),
                                                                                    attr='tax_line_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='tax_group_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='l10n_ar_tribute_afip_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='07', kind=None)],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='tax_lines', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='r', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='r', ctx=Load()),
                                                                                    attr='tax_line_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='tax_group_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='l10n_ar_tribute_afip_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='08', kind=None)],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='tax_lines', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='r', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='r', ctx=Load()),
                                                                                    attr='tax_line_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='tax_group_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='l10n_ar_tribute_afip_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='04', kind=None)],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='tax_lines', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='r', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='r', ctx=Load()),
                                                                                    attr='tax_line_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='tax_group_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='l10n_ar_tribute_afip_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='99', kind=None)],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='tax_lines', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='r', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='r', ctx=Load()),
                                                                                attr='tax_line_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='tax_group_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='profits_tax_group', ctx=Load())],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='tax_lines', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='r', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='r', ctx=Load()),
                                                                                    attr='tax_line_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='tax_group_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='l10n_ar_tribute_afip_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='06', kind=None)],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='tax_lines', ctx=Load()),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='r', annotation=None, type_comment=None)],
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
                                                                                        value=Attribute(
                                                                                            value=Name(id='r', ctx=Load()),
                                                                                            attr='tax_line_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='tax_group_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='l10n_ar_tribute_afip_code',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='09', kind=None)],
                                                                            ),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='r', ctx=Load()),
                                                                                        attr='tax_line_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='tax_group_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[NotEq()],
                                                                                comparators=[Name(id='profits_tax_group', ctx=Load())],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='amount_field', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
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
                    name='_get_vat',
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
                            value=Constant(value=' Applies on wsfe web service and in the VAT digital books ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vat_taxable', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move.line', kind=None),
                                ctx=Load(),
                            ),
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='tax', ctx=Load()),
                                                                        attr='tax_group_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='l10n_ar_vat_afip_code',
                                                                    ctx=Load(),
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='tax', ctx=Load()),
                                                                            attr='tax_group_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='l10n_ar_vat_afip_code',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotIn()],
                                                                    comparators=[
                                                                        List(
                                                                            elts=[
                                                                                Constant(value='0', kind=None),
                                                                                Constant(value='1', kind=None),
                                                                                Constant(value='2', kind=None),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='tax', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='tax_line_id',
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
                                            Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Constant(value='price_subtotal', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='vat_taxable', ctx=Store()),
                                            op=BitOr(),
                                            value=Name(id='line', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='tax_group', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='vat_taxable', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tax_group_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='base_imp', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='invoice_line_ids',
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
                                                                body=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='x', ctx=Load()),
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
                                                                                args=[arg(arg='y', annotation=None, type_comment=None)],
                                                                                vararg=None,
                                                                                kwonlyargs=[],
                                                                                kw_defaults=[],
                                                                                kwarg=None,
                                                                                defaults=[],
                                                                            ),
                                                                            body=Compare(
                                                                                left=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='y', ctx=Load()),
                                                                                        attr='tax_group_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='l10n_ar_vat_afip_code',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='tax_group', ctx=Load()),
                                                                                        attr='l10n_ar_vat_afip_code',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='price_subtotal', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='imp', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='vat_taxable', ctx=Load()),
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
                                                                        value=Attribute(
                                                                            value=Name(id='x', ctx=Load()),
                                                                            attr='tax_group_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='l10n_ar_vat_afip_code',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='tax_group', ctx=Load()),
                                                                            attr='l10n_ar_vat_afip_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='price_subtotal', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='res', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='Id', kind=None),
                                                    Constant(value='BaseImp', kind=None),
                                                    Constant(value='Importe', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='tax_group', ctx=Load()),
                                                        attr='l10n_ar_vat_afip_code',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='base_imp', ctx=Load()),
                                                    Name(id='imp', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vat_base_0', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice_line_ids',
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
                                                        body=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
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
                                                                        args=[arg(arg='y', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='y', ctx=Load()),
                                                                                attr='tax_group_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='l10n_ar_vat_afip_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='3', kind=None)],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='price_subtotal', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='vat_base_0', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='res', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='Id', kind=None),
                                                    Constant(value='BaseImp', kind=None),
                                                    Constant(value='Importe', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='3', kind=None),
                                                    Name(id='vat_base_0', ctx=Load()),
                                                    Constant(value=0.0, kind=None),
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
                            value=IfExp(
                                test=Name(id='res', ctx=Load()),
                                body=Name(id='res', ctx=Load()),
                                orelse=List(elts=[], ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_name_invoice_report',
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
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='l10n_latam_use_documents',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='account_fiscal_country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='AR', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='l10n_ar.report_invoice_document', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_name_invoice_report',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_l10n_ar_get_invoice_totals_for_report',
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
                            targets=[
                                Name(id='tax_ids_filter', ctx=Store()),
                                Name(id='tax_line_id_filter', ctx=Store()),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='include_vat', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_l10n_ar_include_vat',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='include_vat', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='tax_ids_filter', ctx=Store())],
                                    value=Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='aml', annotation=None, type_comment=None),
                                                arg(arg='tax', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='tax', ctx=Load()),
                                                            attr='tax_group_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='l10n_ar_vat_afip_code',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tax_line_id_filter', ctx=Store())],
                                    value=Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='aml', annotation=None, type_comment=None),
                                                arg(arg='tax', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='tax', ctx=Load()),
                                                            attr='tax_group_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='l10n_ar_vat_afip_code',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='tax_lines_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_tax_lines_data_for_totals_from_invoice',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tax_ids_filter',
                                        value=Name(id='tax_ids_filter', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='tax_line_id_filter',
                                        value=Name(id='tax_line_id_filter', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='include_vat', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='amount_untaxed', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='amount_total',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='sum', ctx=Load()),
                                                    args=[
                                                        ListComp(
                                                            elt=Subscript(
                                                                value=Name(id='x', ctx=Load()),
                                                                slice=Constant(value='tax_amount', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='x', ctx=Store()),
                                                                    iter=Name(id='tax_lines_data', ctx=Load()),
                                                                    ifs=[
                                                                        Compare(
                                                                            left=Constant(value='tax_amount', kind=None),
                                                                            ops=[In()],
                                                                            comparators=[Name(id='x', ctx=Load())],
                                                                        ),
                                                                    ],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
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
                                    targets=[Name(id='amount_untaxed', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='amount_untaxed',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_tax_totals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='tax_lines_data', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='amount_total',
                                        ctx=Load(),
                                    ),
                                    Name(id='amount_untaxed', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
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
                    name='_l10n_ar_include_vat',
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
                            value=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='l10n_latam_document_type_id',
                                        ctx=Load(),
                                    ),
                                    attr='l10n_ar_letter',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='B', kind=None),
                                            Constant(value='C', kind=None),
                                            Constant(value='X', kind=None),
                                            Constant(value='R', kind=None),
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
