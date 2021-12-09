Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
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
            name='AccountChartTemplate',
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
                    value=Constant(value='account.chart.template', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_demo_data',
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
                            value=Yield(
                                value=Tuple(
                                    elts=[
                                        Constant(value='res.partner', kind=None),
                                        Dict(
                                            keys=[
                                                Constant(value='base.res_partner_12', kind=None),
                                                Constant(value='base.res_partner_2', kind=None),
                                            ],
                                            values=[
                                                Dict(
                                                    keys=[Constant(value='l10n_cl_sii_taxpayer_type', kind=None)],
                                                    values=[Constant(value='4', kind=None)],
                                                ),
                                                Dict(
                                                    keys=[Constant(value='l10n_cl_sii_taxpayer_type', kind=None)],
                                                    values=[Constant(value='4', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        Expr(
                            value=Yield(
                                value=Tuple(
                                    elts=[
                                        Constant(value='l10n_latam.document.type', kind=None),
                                        Dict(
                                            keys=[Constant(value='l10n_cl.dc_fe_dte', kind=None)],
                                            values=[
                                                Dict(
                                                    keys=[Constant(value='active', kind=None)],
                                                    values=[Constant(value=True, kind=None)],
                                                ),
                                            ],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='model', ctx=Store()),
                                    Name(id='data', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_demo_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Tuple(
                                            elts=[
                                                Name(id='model', ctx=Load()),
                                                Name(id='data', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
                    name='_get_demo_data_move',
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
                            targets=[Name(id='ref', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='ref',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cid', ctx=Store())],
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
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='foreign', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id='ref', ctx=Load()),
                                    args=[Constant(value='l10n_cl.dc_fe_dte', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='model', ctx=Store()),
                                        Name(id='data', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_demo_data_move',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
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
                                                            Constant(value='purchase', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='company',
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
                                        keywords=[],
                                    ),
                                    attr='l10n_latam_use_documents',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=JoinedStr(
                                            values=[
                                                FormattedValue(
                                                    value=Name(id='cid', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value='_demo_invoice_1', kind=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='l10n_latam_document_type_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='foreign', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=JoinedStr(
                                            values=[
                                                FormattedValue(
                                                    value=Name(id='cid', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value='_demo_invoice_2', kind=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='l10n_latam_document_type_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='foreign', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=JoinedStr(
                                            values=[
                                                FormattedValue(
                                                    value=Name(id='cid', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value='_demo_invoice_3', kind=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='l10n_latam_document_type_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='foreign', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=JoinedStr(
                                            values=[
                                                FormattedValue(
                                                    value=Name(id='cid', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value='_demo_invoice_followup', kind=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='l10n_latam_document_type_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='foreign', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='model', ctx=Load()),
                                    Name(id='data', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
