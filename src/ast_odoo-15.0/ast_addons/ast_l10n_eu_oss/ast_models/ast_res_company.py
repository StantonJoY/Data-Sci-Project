Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='eu_tax_map',
            names=[alias(name='EU_TAX_MAP', asname=None)],
            level=1,
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        ClassDef(
            name='Company',
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
                    name='_map_all_eu_companies_taxes',
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
                            value=Constant(value=' Identifies EU companies and calls the _map_eu_taxes function\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='eu_countries', ctx=Store())],
                            value=Attribute(
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
                                    args=[Constant(value='base.europe', kind=None)],
                                    keywords=[],
                                ),
                                attr='country_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='companies', ctx=Store())],
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
                                                    Constant(value='account_fiscal_country_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='eu_countries', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='companies', ctx=Load()),
                                    attr='_map_eu_taxes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
                    name='_map_eu_taxes',
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
                            value=Constant(value="Creates or updates Fiscal Positions for each EU country excluding the company's account_fiscal_country_id\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='eu_countries', ctx=Store())],
                            value=Attribute(
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
                                    args=[Constant(value='base.europe', kind=None)],
                                    keywords=[],
                                ),
                                attr='country_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='oss_tax_groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
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
                                                    Constant(value='module', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='l10n_eu_oss', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='account.tax.group', kind=None),
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
                        For(
                            target=Name(id='company', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='invoice_repartition_lines', ctx=Store()),
                                                Name(id='refund_repartition_lines', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='_get_repartition_lines_oss',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='taxes', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='type_tax_use', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='sale', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='amount_type', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='percent', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
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
                                                            Constant(value='country_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='company', ctx=Load()),
                                                                    attr='account_fiscal_country_id',
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
                                                            Constant(value='tax_group_id', kind=None),
                                                            Constant(value='not in', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='oss_tax_groups', ctx=Load()),
                                                                    attr='mapped',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='res_id', kind=None)],
                                                                keywords=[],
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
                                    targets=[Name(id='multi_tax_reports_countries_fpos', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
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
                                                            Constant(value='foreign_vat', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
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
                                    targets=[Name(id='oss_countries', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Name(id='eu_countries', ctx=Load()),
                                            op=Sub(),
                                            right=Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='account_fiscal_country_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='multi_tax_reports_countries_fpos', ctx=Load()),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='country', ctx=Store()),
                                    iter=Name(id='oss_countries', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='mapping', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='fpos', ctx=Store())],
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
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='country_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='country', ctx=Load()),
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
                                                                    Constant(value='auto_apply', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='vat_required', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='foreign_vat', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
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
                                                operand=Name(id='fpos', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='fpos', ctx=Store())],
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
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='country_id', kind=None),
                                                                    Constant(value='company_id', kind=None),
                                                                    Constant(value='auto_apply', kind=None),
                                                                ],
                                                                values=[
                                                                    BinOp(
                                                                        left=Constant(value='OSS B2C %s', kind=None),
                                                                        op=Mod(),
                                                                        right=Attribute(
                                                                            value=Name(id='country', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='country', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='company', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='foreign_taxes', ctx=Store())],
                                            value=DictComp(
                                                key=Attribute(
                                                    value=Name(id='tax', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                value=Name(id='tax', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='tax', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fpos', ctx=Load()),
                                                                attr='tax_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tax_dest_id',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='tax', ctx=Load()),
                                                                    attr='amount_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='percent', kind=None)],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='domestic_tax', ctx=Store()),
                                            iter=Name(id='taxes', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='tax_amount', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='EU_TAX_MAP', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='company', ctx=Load()),
                                                                            attr='account_fiscal_country_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='code',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='domestic_tax', ctx=Load()),
                                                                        attr='amount',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='country', ctx=Load()),
                                                                        attr='code',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='tax_amount', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='domestic_tax', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='fpos', ctx=Load()),
                                                                            attr='tax_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='tax_src_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='foreign_taxes', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Name(id='tax_amount', ctx=Load()),
                                                                        Constant(value=False, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='tax_group_fid', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Constant(value='oss_tax_group_%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Call(
                                                                            func=Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='str', ctx=Load()),
                                                                                    args=[Name(id='tax_amount', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='replace',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Constant(value='.', kind=None),
                                                                                Constant(value='_', kind=None),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=UnaryOp(
                                                                        op=Not(),
                                                                        operand=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='ref',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                BinOp(
                                                                                    left=Constant(value='l10n_eu_oss.%s', kind=None),
                                                                                    op=Mod(),
                                                                                    right=Name(id='tax_group_fid', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='raise_if_not_found',
                                                                                    value=Constant(value=False, kind=None),
                                                                                ),
                                                                            ],
                                                                        ),
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
                                                                                        slice=Constant(value='ir.model.data', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='create',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='name', kind=None),
                                                                                            Constant(value='module', kind=None),
                                                                                            Constant(value='model', kind=None),
                                                                                            Constant(value='res_id', kind=None),
                                                                                            Constant(value='noupdate', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Name(id='tax_group_fid', ctx=Load()),
                                                                                            Constant(value='l10n_eu_oss', kind=None),
                                                                                            Constant(value='account.tax.group', kind=None),
                                                                                            Attribute(
                                                                                                value=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Subscript(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='env',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            slice=Constant(value='account.tax.group', kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='create',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[
                                                                                                        Dict(
                                                                                                            keys=[Constant(value='name', kind=None)],
                                                                                                            values=[
                                                                                                                BinOp(
                                                                                                                    left=Constant(value='OSS %s%%', kind=None),
                                                                                                                    op=Mod(),
                                                                                                                    right=Name(id='tax_amount', ctx=Load()),
                                                                                                                ),
                                                                                                            ],
                                                                                                        ),
                                                                                                    ],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='foreign_taxes', ctx=Load()),
                                                                            slice=Name(id='tax_amount', ctx=Load()),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
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
                                                                            attr='create',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='name', kind=None),
                                                                                    Constant(value='amount', kind=None),
                                                                                    Constant(value='invoice_repartition_line_ids', kind=None),
                                                                                    Constant(value='refund_repartition_line_ids', kind=None),
                                                                                    Constant(value='type_tax_use', kind=None),
                                                                                    Constant(value='description', kind=None),
                                                                                    Constant(value='tax_group_id', kind=None),
                                                                                    Constant(value='country_id', kind=None),
                                                                                    Constant(value='sequence', kind=None),
                                                                                    Constant(value='company_id', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    BinOp(
                                                                                        left=Constant(value='%(rate)s%% %(country)s %(label)s', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Dict(
                                                                                            keys=[
                                                                                                Constant(value='rate', kind=None),
                                                                                                Constant(value='country', kind=None),
                                                                                                Constant(value='label', kind=None),
                                                                                            ],
                                                                                            values=[
                                                                                                Name(id='tax_amount', ctx=Load()),
                                                                                                Attribute(
                                                                                                    value=Name(id='country', ctx=Load()),
                                                                                                    attr='code',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                Attribute(
                                                                                                    value=Name(id='country', ctx=Load()),
                                                                                                    attr='vat_label',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                    Name(id='tax_amount', ctx=Load()),
                                                                                    Name(id='invoice_repartition_lines', ctx=Load()),
                                                                                    Name(id='refund_repartition_lines', ctx=Load()),
                                                                                    Constant(value='sale', kind=None),
                                                                                    BinOp(
                                                                                        left=Constant(value='%s%%', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Name(id='tax_amount', ctx=Load()),
                                                                                    ),
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
                                                                                            args=[
                                                                                                BinOp(
                                                                                                    left=Constant(value='l10n_eu_oss.%s', kind=None),
                                                                                                    op=Mod(),
                                                                                                    right=Name(id='tax_group_fid', ctx=Load()),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='company', ctx=Load()),
                                                                                            attr='account_fiscal_country_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=1000, kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='company', ctx=Load()),
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
                                                            orelse=[],
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='mapping', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='tax_src_id', kind=None),
                                                                                    Constant(value='tax_dest_id', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Name(id='domestic_tax', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='foreign_taxes', ctx=Load()),
                                                                                            slice=Name(id='tax_amount', ctx=Load()),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='mapping', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='fpos', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='tax_ids', kind=None)],
                                                                values=[Name(id='mapping', ctx=Load())],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_repartition_lines_oss',
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
                            targets=[Name(id='defaults', ctx=Store())],
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
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='oss_account', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_oss_account',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='oss_account', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='defaults', ctx=Load()),
                                                        slice=Constant(value='invoice_repartition_line_ids', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='account_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='oss_account', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='defaults', ctx=Load()),
                                                        slice=Constant(value='refund_repartition_line_ids', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='account_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='oss_account', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='oss_tag', ctx=Store())],
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
                                args=[Constant(value='l10n_eu_oss.tag_oss', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='orm_command', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='itertools', ctx=Load()),
                                    attr='chain',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='defaults', ctx=Load()),
                                        slice=Constant(value='invoice_repartition_line_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='defaults', ctx=Load()),
                                        slice=Constant(value='refund_repartition_line_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rep_line_vals', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='orm_command', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rep_line_vals', ctx=Load()),
                                            slice=Constant(value='tag_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='rep_line_vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='tag_ids', kind=None),
                                                List(elts=[], ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=List(
                                            elts=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='Command', ctx=Load()),
                                                        attr='link',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='oss_tag', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='defaults', ctx=Load()),
                                        slice=Constant(value='invoice_repartition_line_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='defaults', ctx=Load()),
                                        slice=Constant(value='refund_repartition_line_ids', kind=None),
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
                    name='_get_oss_account',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        BinOp(
                                            left=Constant(value='l10n_eu_oss.oss_tax_account_company_%s', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='raise_if_not_found',
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sales_tax_accounts', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
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
                                                        attr='search',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='type_tax_use', kind=None),
                                                                        Constant(value='=', kind=None),
                                                                        Constant(value='sale', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='company_id', kind=None),
                                                                        Constant(value='=', kind=None),
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
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
                                                attr='invoice_repartition_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='account_id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='sales_tax_accounts', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='new_code', ctx=Store())],
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
                                            attr='_search_new_account_code',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='sales_tax_accounts', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='sales_tax_accounts', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='oss_account', ctx=Store())],
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
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='code', kind=None),
                                                    Constant(value='user_type_id', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='%s OSS', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='sales_tax_accounts', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='new_code', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='sales_tax_accounts', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='user_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
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
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.model.data', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value='model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='noupdate', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='oss_tax_account_company_%s', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='l10n_eu_oss', kind=None),
                                                    Constant(value='account.account', kind=None),
                                                    Attribute(
                                                        value=Name(id='oss_account', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=True, kind=None),
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
                                args=[
                                    BinOp(
                                        left=Constant(value='l10n_eu_oss.oss_tax_account_company_%s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
