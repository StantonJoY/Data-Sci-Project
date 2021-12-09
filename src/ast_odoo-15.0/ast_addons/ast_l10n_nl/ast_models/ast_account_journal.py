Module(
    body=[
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
        ClassDef(
            name='AccountJournal',
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
                    value=Constant(value='account.journal', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_fill_missing_values',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_fill_missing_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='vals', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='type', kind=None)],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='purchase', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='vals', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='company_id', kind=None)],
                                    keywords=[],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.company', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='company_id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='company',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='country_id',
                                        ctx=Load(),
                                    ),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='NL', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='type_control_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='type_control_ids', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='type_control_ids', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
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
                                                    args=[Constant(value='account.data_account_type_direct_costs', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='type_control_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Name(id='type_control_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                    name='_prepare_liquidity_account_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
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
                            targets=[Name(id='account_vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_prepare_liquidity_account_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='company', ctx=Load()),
                                    Name(id='code', ctx=Load()),
                                    Name(id='vals', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='account_fiscal_country_id',
                                        ctx=Load(),
                                    ),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='NL', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='account_vals', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='tag_ids', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='account_vals', ctx=Load()),
                                                slice=Constant(value='tag_ids', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=4, kind=None),
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
                                                            args=[Constant(value='l10n_nl.account_tag_25', kind=None)],
                                                            keywords=[],
                                                        ),
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='account_vals', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
