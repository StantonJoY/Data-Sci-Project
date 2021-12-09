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
                        If(
                            test=Compare(
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
                                comparators=[Constant(value='EC', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='document_type', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Name(id='ref', ctx=Load()),
                                                        args=[
                                                            Constant(value='l10n_ec.ec_dt_18', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='l10n_ec.ec_dt_18', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
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
                                    value=Name(id='document_type', ctx=Load()),
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
                                    value=Name(id='document_type', ctx=Load()),
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
                                    value=Name(id='document_type', ctx=Load()),
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
                                    value=Name(id='document_type', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
