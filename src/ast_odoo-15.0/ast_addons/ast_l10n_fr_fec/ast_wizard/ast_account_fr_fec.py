Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_is_zero', asname=None),
                alias(name='pycompat', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='AccountFrFec',
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
                    value=Constant(value='account.fr.fec', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Ficher Echange Informatise', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_from', ctx=Store())],
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
                                value=Constant(value='Start Date', kind=None),
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
                    targets=[Name(id='date_to', ctx=Store())],
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
                                value=Constant(value='End Date', kind=None),
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
                    targets=[Name(id='fec_data', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='FEC File', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='attachment',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='filename', ctx=Store())],
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
                                value=Constant(value='Filename', kind=None),
                            ),
                            keyword(
                                arg='size',
                                value=Constant(value=256, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='test_file', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='export_type', ctx=Store())],
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
                                            Constant(value='official', kind=None),
                                            Constant(value='Official FEC report (posted entries only)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='nonofficial', kind=None),
                                            Constant(value='Non-official FEC report (posted and unposted entries)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Export Type', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='official', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_export_file',
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
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='test_file',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='export_type',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='official', kind=None),
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
                            args=[Constant(value='test_file', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='do_query_unaffected_earnings',
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
                            value=Constant(value=' Compute the sum of ending balances for all accounts that are of a type that does not bring forward the balance in new fiscal years.\n            This is needed because we have to display only one line for the initial balance of all expense/revenue accounts in the FEC.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sql_query', ctx=Store())],
                            value=Constant(value="\n        SELECT\n            'OUV' AS JournalCode,\n            'Balance initiale' AS JournalLib,\n            'OUVERTURE/' || %s AS EcritureNum,\n            %s AS EcritureDate,\n            '120/129' AS CompteNum,\n            'Benefice (perte) reporte(e)' AS CompteLib,\n            '' AS CompAuxNum,\n            '' AS CompAuxLib,\n            '-' AS PieceRef,\n            %s AS PieceDate,\n            '/' AS EcritureLib,\n            replace(CASE WHEN COALESCE(sum(aml.balance), 0) <= 0 THEN '0,00' ELSE to_char(SUM(aml.balance), '000000000000000D99') END, '.', ',') AS Debit,\n            replace(CASE WHEN COALESCE(sum(aml.balance), 0) >= 0 THEN '0,00' ELSE to_char(-SUM(aml.balance), '000000000000000D99') END, '.', ',') AS Credit,\n            '' AS EcritureLet,\n            '' AS DateLet,\n            %s AS ValidDate,\n            '' AS Montantdevise,\n            '' AS Idevise\n        FROM\n            account_move_line aml\n            LEFT JOIN account_move am ON am.id=aml.move_id\n            JOIN account_account aa ON aa.id = aml.account_id\n            LEFT JOIN account_account_type aat ON aa.user_type_id = aat.id\n        WHERE\n            am.date < %s\n            AND am.company_id = %s\n            AND aat.include_initial_balance IS NOT TRUE\n            AND (aml.debit != 0 OR aml.credit != 0)\n        ", kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='official', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='sql_query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value="\n            AND am.state = 'posted'\n            ", kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='company',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='formatted_date_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='date_from',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_from', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='date_from',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='formatted_date_year', ctx=Store())],
                            value=Attribute(
                                value=Name(id='date_from', ctx=Load()),
                                attr='year',
                                ctx=Load(),
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
                                    Name(id='sql_query', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='formatted_date_year', ctx=Load()),
                                            Name(id='formatted_date_from', ctx=Load()),
                                            Name(id='formatted_date_from', ctx=Load()),
                                            Name(id='formatted_date_from', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='date_from',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='listrow', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='row', ctx=Store())],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='listrow', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[Name(id='row', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='listrow', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_company_legal_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Dom-Tom are excluded from the EU's fiscal territory\n        Those regions do not have SIREN\n        sources:\n            https://www.service-public.fr/professionnels-entreprises/vosdroits/F23570\n            http://www.douane.gouv.fr/articles/a11024-tva-dans-les-dom\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='dom_tom_group', ctx=Store())],
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
                                args=[Constant(value='l10n_fr.dom-tom', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_dom_tom', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='account_fiscal_country_id',
                                        ctx=Load(),
                                    ),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='dom_tom_group', ctx=Load()),
                                                attr='country_ids',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='code', kind=None)],
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
                                        operand=Name(id='is_dom_tom', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='vat',
                                            ctx=Load(),
                                        ),
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
                                                args=[
                                                    Constant(value='Missing VAT number for company %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='company', ctx=Load()),
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
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='is_dom_tom', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=Constant(value=0, kind=None),
                                                upper=Constant(value=2, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='FR', kind=None)],
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
                                                args=[Constant(value='FEC is for French companies only !', kind=None)],
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
                        Return(
                            value=Dict(
                                keys=[Constant(value='siren', kind=None)],
                                values=[
                                    IfExp(
                                        test=UnaryOp(
                                            op=Not(),
                                            operand=Name(id='is_dom_tom', ctx=Load()),
                                        ),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=Constant(value=4, kind=None),
                                                upper=Constant(value=13, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value='', kind=None),
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
                    name='generate_fec',
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='date_from',
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Name(id='today', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='date_to',
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Name(id='today', ctx=Load())],
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
                                                args=[Constant(value='You could not set the start date or the end date in the future.', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='date_from',
                                    ctx=Load(),
                                ),
                                ops=[GtE()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='date_to',
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
                                                args=[Constant(value='The start date must be inferior to the end date.', kind=None)],
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
                            targets=[Name(id='company', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='company',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_legal_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_company_legal_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='company', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='header', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='JournalCode', kind='u'),
                                    Constant(value='JournalLib', kind='u'),
                                    Constant(value='EcritureNum', kind='u'),
                                    Constant(value='EcritureDate', kind='u'),
                                    Constant(value='CompteNum', kind='u'),
                                    Constant(value='CompteLib', kind='u'),
                                    Constant(value='CompAuxNum', kind='u'),
                                    Constant(value='CompAuxLib', kind='u'),
                                    Constant(value='PieceRef', kind='u'),
                                    Constant(value='PieceDate', kind='u'),
                                    Constant(value='EcritureLib', kind='u'),
                                    Constant(value='Debit', kind='u'),
                                    Constant(value='Credit', kind='u'),
                                    Constant(value='EcritureLet', kind='u'),
                                    Constant(value='DateLet', kind='u'),
                                    Constant(value='ValidDate', kind='u'),
                                    Constant(value='Montantdevise', kind='u'),
                                    Constant(value='Idevise', kind='u'),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rows_to_write', ctx=Store())],
                            value=List(
                                elts=[Name(id='header', ctx=Load())],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='unaffected_earnings_xml_ref', ctx=Store())],
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
                                args=[Constant(value='account.data_unaffected_earnings', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='unaffected_earnings_line', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='unaffected_earnings_xml_ref', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='unaffected_earnings_results', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='do_query_unaffected_earnings',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='unaffected_earnings_line', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='sql_query', ctx=Store())],
                            value=Constant(value="\n        SELECT\n            'OUV' AS JournalCode,\n            'Balance initiale' AS JournalLib,\n            'OUVERTURE/' || %s AS EcritureNum,\n            %s AS EcritureDate,\n            MIN(aa.code) AS CompteNum,\n            replace(replace(MIN(aa.name), '|', '/'), '\t', '') AS CompteLib,\n            '' AS CompAuxNum,\n            '' AS CompAuxLib,\n            '-' AS PieceRef,\n            %s AS PieceDate,\n            '/' AS EcritureLib,\n            replace(CASE WHEN sum(aml.balance) <= 0 THEN '0,00' ELSE to_char(SUM(aml.balance), '000000000000000D99') END, '.', ',') AS Debit,\n            replace(CASE WHEN sum(aml.balance) >= 0 THEN '0,00' ELSE to_char(-SUM(aml.balance), '000000000000000D99') END, '.', ',') AS Credit,\n            '' AS EcritureLet,\n            '' AS DateLet,\n            %s AS ValidDate,\n            '' AS Montantdevise,\n            '' AS Idevise,\n            MIN(aa.id) AS CompteID\n        FROM\n            account_move_line aml\n            LEFT JOIN account_move am ON am.id=aml.move_id\n            JOIN account_account aa ON aa.id = aml.account_id\n            LEFT JOIN account_account_type aat ON aa.user_type_id = aat.id\n        WHERE\n            am.date < %s\n            AND am.company_id = %s\n            AND aat.include_initial_balance = 't'\n            AND (aml.debit != 0 OR aml.credit != 0)\n        ", kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='official', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='sql_query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value="\n            AND am.state = 'posted'\n            ", kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='sql_query', ctx=Store()),
                            op=Add(),
                            value=Constant(value="\n        GROUP BY aml.account_id, aat.type\n        HAVING round(sum(aml.balance), %s) != 0\n        AND aat.type not in ('receivable', 'payable')\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='formatted_date_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='date_from',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_from', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='date_from',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='formatted_date_year', ctx=Store())],
                            value=Attribute(
                                value=Name(id='date_from', ctx=Load()),
                                attr='year',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency_digits', ctx=Store())],
                            value=Constant(value=2, kind=None),
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
                                    Name(id='sql_query', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='formatted_date_year', ctx=Load()),
                                            Name(id='formatted_date_from', ctx=Load()),
                                            Name(id='formatted_date_from', ctx=Load()),
                                            Name(id='formatted_date_from', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='date_from',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='currency_digits', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='listrow', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='row', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='account_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='listrow', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='unaffected_earnings_line', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='account', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.account', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='account_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='account', ctx=Load()),
                                                        attr='user_type_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
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
                                                            args=[Constant(value='account.data_unaffected_earnings', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='unaffected_earnings_line', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='current_amount', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Name(id='float', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='listrow', ctx=Load()),
                                                                            slice=Constant(value=11, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='replace',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value=',', kind=None),
                                                                        Constant(value='.', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='float', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='listrow', ctx=Load()),
                                                                            slice=Constant(value=12, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='replace',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value=',', kind=None),
                                                                        Constant(value='.', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='unaffected_earnings_amount', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Name(id='float', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='unaffected_earnings_results', ctx=Load()),
                                                                            slice=Constant(value=11, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='replace',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value=',', kind=None),
                                                                        Constant(value='.', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='float', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='unaffected_earnings_results', ctx=Load()),
                                                                            slice=Constant(value=12, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='replace',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value=',', kind=None),
                                                                        Constant(value='.', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='listrow_amount', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='current_amount', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='unaffected_earnings_amount', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Call(
                                                        func=Name(id='float_is_zero', ctx=Load()),
                                                        args=[Name(id='listrow_amount', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Name(id='currency_digits', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='listrow_amount', ctx=Load()),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='listrow', ctx=Load()),
                                                                    slice=Constant(value=11, kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[Name(id='listrow_amount', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='.', kind=None),
                                                                    Constant(value=',', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='listrow', ctx=Load()),
                                                                    slice=Constant(value=12, kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='0,00', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='listrow', ctx=Load()),
                                                                    slice=Constant(value=11, kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='0,00', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='listrow', ctx=Load()),
                                                                    slice=Constant(value=12, kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Name(id='listrow_amount', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='.', kind=None),
                                                                    Constant(value=',', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rows_to_write', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='listrow', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='unaffected_earnings_line', ctx=Load()),
                                    ),
                                    Name(id='unaffected_earnings_results', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='unaffected_earnings_results', ctx=Load()),
                                                    slice=Constant(value=11, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='0,00', kind=None)],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='unaffected_earnings_results', ctx=Load()),
                                                    slice=Constant(value=12, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='0,00', kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='unaffected_earnings_account', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.account', kind=None),
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
                                                                    args=[Constant(value='account.data_unaffected_earnings', kind=None)],
                                                                    keywords=[],
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
                                If(
                                    test=Name(id='unaffected_earnings_account', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='unaffected_earnings_results', ctx=Load()),
                                                    slice=Constant(value=4, kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='unaffected_earnings_account', ctx=Load()),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='unaffected_earnings_results', ctx=Load()),
                                                    slice=Constant(value=5, kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='unaffected_earnings_account', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rows_to_write', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='unaffected_earnings_results', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='sql_query', ctx=Store())],
                            value=Constant(value="\n        SELECT\n            'OUV' AS JournalCode,\n            'Balance initiale' AS JournalLib,\n            'OUVERTURE/' || %s AS EcritureNum,\n            %s AS EcritureDate,\n            MIN(aa.code) AS CompteNum,\n            replace(MIN(aa.name), '|', '/') AS CompteLib,\n            CASE WHEN MIN(aat.type) IN ('receivable', 'payable')\n            THEN\n                CASE WHEN rp.ref IS null OR rp.ref = ''\n                THEN rp.id::text\n                ELSE replace(rp.ref, '|', '/')\n                END\n            ELSE ''\n            END\n            AS CompAuxNum,\n            CASE WHEN aat.type IN ('receivable', 'payable')\n            THEN COALESCE(replace(rp.name, '|', '/'), '')\n            ELSE ''\n            END AS CompAuxLib,\n            '-' AS PieceRef,\n            %s AS PieceDate,\n            '/' AS EcritureLib,\n            replace(CASE WHEN sum(aml.balance) <= 0 THEN '0,00' ELSE to_char(SUM(aml.balance), '000000000000000D99') END, '.', ',') AS Debit,\n            replace(CASE WHEN sum(aml.balance) >= 0 THEN '0,00' ELSE to_char(-SUM(aml.balance), '000000000000000D99') END, '.', ',') AS Credit,\n            '' AS EcritureLet,\n            '' AS DateLet,\n            %s AS ValidDate,\n            '' AS Montantdevise,\n            '' AS Idevise,\n            MIN(aa.id) AS CompteID\n        FROM\n            account_move_line aml\n            LEFT JOIN account_move am ON am.id=aml.move_id\n            LEFT JOIN res_partner rp ON rp.id=aml.partner_id\n            JOIN account_account aa ON aa.id = aml.account_id\n            LEFT JOIN account_account_type aat ON aa.user_type_id = aat.id\n        WHERE\n            am.date < %s\n            AND am.company_id = %s\n            AND aat.include_initial_balance = 't'\n            AND (aml.debit != 0 OR aml.credit != 0)\n        ", kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='official', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='sql_query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value="\n            AND am.state = 'posted'\n            ", kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='sql_query', ctx=Store()),
                            op=Add(),
                            value=Constant(value="\n        GROUP BY aml.account_id, aat.type, rp.ref, rp.id\n        HAVING round(sum(aml.balance), %s) != 0\n        AND aat.type in ('receivable', 'payable')\n        ", kind=None),
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
                                    Name(id='sql_query', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='formatted_date_year', ctx=Load()),
                                            Name(id='formatted_date_from', ctx=Load()),
                                            Name(id='formatted_date_from', ctx=Load()),
                                            Name(id='formatted_date_from', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='date_from',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='currency_digits', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='listrow', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='row', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='account_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='listrow', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rows_to_write', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='listrow', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sql_query', ctx=Store())],
                            value=Constant(value="\n        SELECT\n            replace(replace(aj.code, '|', '/'), '\t', '') AS JournalCode,\n            replace(replace(aj.name, '|', '/'), '\t', '') AS JournalLib,\n            replace(replace(am.name, '|', '/'), '\t', '') AS EcritureNum,\n            TO_CHAR(am.date, 'YYYYMMDD') AS EcritureDate,\n            aa.code AS CompteNum,\n            replace(replace(aa.name, '|', '/'), '\t', '') AS CompteLib,\n            CASE WHEN aat.type IN ('receivable', 'payable')\n            THEN\n                CASE WHEN rp.ref IS null OR rp.ref = ''\n                THEN rp.id::text\n                ELSE replace(rp.ref, '|', '/')\n                END\n            ELSE ''\n            END\n            AS CompAuxNum,\n            CASE WHEN aat.type IN ('receivable', 'payable')\n            THEN COALESCE(replace(replace(rp.name, '|', '/'), '\t', ''), '')\n            ELSE ''\n            END AS CompAuxLib,\n            CASE WHEN am.ref IS null OR am.ref = ''\n            THEN '-'\n            ELSE replace(replace(am.ref, '|', '/'), '\t', '')\n            END\n            AS PieceRef,\n            TO_CHAR(am.date, 'YYYYMMDD') AS PieceDate,\n            CASE WHEN aml.name IS NULL OR aml.name = '' THEN '/'\n                WHEN aml.name SIMILAR TO '[\t|\\s|\n]*' THEN '/'\n                ELSE replace(replace(replace(replace(aml.name, '|', '/'), '\t', ''), '\n', ''), '\r', '') END AS EcritureLib,\n            replace(CASE WHEN aml.debit = 0 THEN '0,00' ELSE to_char(aml.debit, '000000000000000D99') END, '.', ',') AS Debit,\n            replace(CASE WHEN aml.credit = 0 THEN '0,00' ELSE to_char(aml.credit, '000000000000000D99') END, '.', ',') AS Credit,\n            CASE WHEN rec.name IS NULL THEN '' ELSE rec.name END AS EcritureLet,\n            CASE WHEN aml.full_reconcile_id IS NULL THEN '' ELSE TO_CHAR(rec.create_date, 'YYYYMMDD') END AS DateLet,\n            TO_CHAR(am.date, 'YYYYMMDD') AS ValidDate,\n            CASE\n                WHEN aml.amount_currency IS NULL OR aml.amount_currency = 0 THEN ''\n                ELSE replace(to_char(aml.amount_currency, '000000000000000D99'), '.', ',')\n            END AS Montantdevise,\n            CASE WHEN aml.currency_id IS NULL THEN '' ELSE rc.name END AS Idevise\n        FROM\n            account_move_line aml\n            LEFT JOIN account_move am ON am.id=aml.move_id\n            LEFT JOIN res_partner rp ON rp.id=aml.partner_id\n            JOIN account_journal aj ON aj.id = am.journal_id\n            JOIN account_account aa ON aa.id = aml.account_id\n            LEFT JOIN account_account_type aat ON aa.user_type_id = aat.id\n            LEFT JOIN res_currency rc ON rc.id = aml.currency_id\n            LEFT JOIN account_full_reconcile rec ON rec.id = aml.full_reconcile_id\n        WHERE\n            am.date >= %s\n            AND am.date <= %s\n            AND am.company_id = %s\n            AND (aml.debit != 0 OR aml.credit != 0)\n        ", kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='official', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='sql_query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value="\n            AND am.state = 'posted'\n            ", kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='sql_query', ctx=Store()),
                            op=Add(),
                            value=Constant(value='\n        ORDER BY\n            am.date,\n            am.name,\n            aml.id\n        ', kind=None),
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
                                    Name(id='sql_query', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='date_from',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='date_to',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
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
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rows_to_write', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[Name(id='row', ctx=Load())],
                                                keywords=[],
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
                            targets=[Name(id='fecvalue', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_csv_write_rows',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rows_to_write', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='date_to',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='suffix', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='nonofficial', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='suffix', ctx=Store())],
                                    value=Constant(value='-NONOFFICIAL', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='fec_data', kind=None),
                                            Constant(value='filename', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='encodebytes',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='fecvalue', ctx=Load())],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                left=Constant(value='%sFEC%s%s.csv', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='company_legal_data', ctx=Load()),
                                                            slice=Constant(value='siren', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='end_date', ctx=Load()),
                                                        Name(id='suffix', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='fiscalyear_lock_date', ctx=Store())],
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
                                attr='fiscalyear_lock_date',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_file',
                                            ctx=Load(),
                                        ),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='fiscalyear_lock_date', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Name(id='fiscalyear_lock_date', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='date_to',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='fiscalyear_lock_date', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='date_to',
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
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='url', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Constant(value='FEC', kind=None),
                                    Constant(value='ir.actions.act_url', kind=None),
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Constant(value='web/content/?model=account.fr.fec&id=', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            op=Add(),
                                            right=Constant(value='&filename_field=filename&field=fec_data&download=true&filename=', kind=None),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filename',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='self', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_csv_write_rows',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rows', annotation=None, type_comment=None),
                            arg(arg='lineterminator', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='\r\n', kind='u')],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Write FEC rows into a file\n        It seems that Bercy's bureaucracy is not too happy about the\n        empty new line at the End Of File.\n\n        @param {list(list)} rows: the list of rows. Each row is a list of strings\n        @param {unicode string} [optional] lineterminator: effective line terminator\n            Has nothing to do with the csv writer parameter\n            The last line written won't be terminated with it\n\n        @return the value of the file\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='fecfile', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_writer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fecfile', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='delimiter',
                                        value=Constant(value='|', kind=None),
                                    ),
                                    keyword(
                                        arg='lineterminator',
                                        value=Constant(value='', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rows_length', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='rows', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='i', ctx=Store()),
                                    Name(id='row', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='rows', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Name(id='i', ctx=Load()),
                                            ops=[Eq()],
                                            comparators=[
                                                BinOp(
                                                    left=Name(id='rows_length', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='lineterminator', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='writerow',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='row', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fecvalue', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fecfile', ctx=Load()),
                                    attr='getvalue',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fecfile', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='fecvalue', ctx=Load()),
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
