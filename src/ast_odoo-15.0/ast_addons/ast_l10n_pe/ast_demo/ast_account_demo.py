Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
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
                        Assign(
                            targets=[Name(id='document_type', ctx=Store())],
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
                                args=[Constant(value='l10n_pe.document_type01', kind=None)],
                                keywords=[],
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
                            value=Attribute(
                                value=Name(id='document_type', ctx=Load()),
                                attr='id',
                                ctx=Load(),
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
                                    slice=Constant(value='l10n_latam_document_number', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='FFI-000001', kind=None),
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
                            value=Attribute(
                                value=Name(id='document_type', ctx=Load()),
                                attr='id',
                                ctx=Load(),
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
                                                Constant(value='_demo_invoice_2', kind=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='l10n_latam_document_number', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='FFI-000002', kind=None),
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
                            value=Attribute(
                                value=Name(id='document_type', ctx=Load()),
                                attr='id',
                                ctx=Load(),
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
                                                Constant(value='_demo_invoice_3', kind=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='l10n_latam_document_number', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='FFI-000003', kind=None),
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
                            value=Attribute(
                                value=Name(id='document_type', ctx=Load()),
                                attr='id',
                                ctx=Load(),
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
                                                Constant(value='_demo_invoice_followup', kind=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='l10n_latam_document_number', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='FFI-000004', kind=None),
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
                                                Constant(value='_demo_invoice_5', kind=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='l10n_latam_document_number', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='1', kind=None),
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
                                                Constant(value='_demo_invoice_equipment_purchase', kind=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='l10n_latam_document_number', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='INV-000089', kind=None),
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
