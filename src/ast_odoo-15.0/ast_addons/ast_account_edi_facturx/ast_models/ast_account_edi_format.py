Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='DEFAULT_SERVER_DATE_FORMAT', asname=None),
                alias(name='float_repr', asname=None),
                alias(name='is_html_empty', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='PyPDF2',
            names=[alias(name='PdfFileReader', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='markupsafe', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
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
        Assign(
            targets=[Name(id='DEFAULT_FACTURX_DATE_FORMAT', ctx=Store())],
            value=Constant(value='%Y%m%d', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='AccountEdiFormat',
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
                    value=Constant(value='account.edi.format', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post_invoice_edi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoices', annotation=None, type_comment=None),
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
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='facturx_1_0_05', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_post_invoice_edi',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoices', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice', ctx=Store()),
                            iter=Name(id='invoices', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_export_facturx',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoice', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Name(id='invoice', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='success', kind=None),
                                            Constant(value='attachment', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Name(id='attachment', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
                    name='_is_embedding_to_invoice_pdf_needed',
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
                            value=IfExp(
                                test=Compare(
                                    left=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value='facturx_1_0_05', kind=None)],
                                ),
                                body=Constant(value=True, kind=None),
                                orelse=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='_is_embedding_to_invoice_pdf_needed',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_embedding_to_invoice_pdf_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_embedding_to_invoice_pdf_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='values', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='facturx_1_0_05', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='factur-x.xml', kind=None),
                                    type_comment=None,
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
                    name='_export_facturx',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='format_date',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='dt', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dt', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='dt', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dt', ctx=Load()),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='DEFAULT_FACTURX_DATE_FORMAT', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='format_monetary',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='number', annotation=None, type_comment=None),
                                    arg(arg='currency', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='float_repr', ctx=Load()),
                                        args=[
                                            Name(id='number', ctx=Load()),
                                            Attribute(
                                                value=Name(id='currency', ctx=Load()),
                                                attr='decimal_places',
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
                            targets=[Name(id='template_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    None,
                                    Constant(value='tax_details', kind=None),
                                    Constant(value='format_date', kind=None),
                                    Constant(value='format_monetary', kind=None),
                                    Constant(value='is_html_empty', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='_prepare_edi_vals_to_export',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='_prepare_edi_tax_details',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='format_date', ctx=Load()),
                                    Name(id='format_monetary', ctx=Load()),
                                    Name(id='is_html_empty', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='markupsafe', ctx=Load()),
                                    attr='Markup',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="<?xml version='1.0' encoding='UTF-8'?>", kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='xml_content', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='account_edi_facturx.account_invoice_facturx_export', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[Name(id='template_values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml_name', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s_facturx.xml', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        attr='replace',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='/', kind=None),
                                        Constant(value='_', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='raw', kind=None),
                                            Constant(value='mimetype', kind=None),
                                        ],
                                        values=[
                                            Name(id='xml_name', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='xml_content', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='application/xml', kind=None),
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
                    name='_is_facturx',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='facturx_1_0_05', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='{urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100}CrossIndustryInvoice', kind=None)],
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
                    name='_create_invoice_from_xml_tree',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_facturx',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_import_facturx',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tree', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move', kind=None),
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_create_invoice_from_xml_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
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
                    name='_update_invoice_from_xml_tree',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_facturx',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_import_facturx',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tree', ctx=Load()),
                                            Name(id='invoice', ctx=Load()),
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_update_invoice_from_xml_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
                                    Name(id='invoice', ctx=Load()),
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
                    name='_import_facturx',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Decodes a factur-x invoice into an invoice.\n\n        :param tree:    the factur-x tree to decode.\n        :param invoice: the invoice to update or an empty recordset.\n        :returns:       the invoice where the factur-x data was imported.\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='_find_value',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='xpath', annotation=None, type_comment=None),
                                    arg(arg='element', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Name(id='tree', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_find_value',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='xpath', ctx=Load()),
                                            Name(id='element', ctx=Load()),
                                            Attribute(
                                                value=Name(id='tree', ctx=Load()),
                                                attr='nsmap',
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
                        Assign(
                            targets=[Name(id='amount_total_import', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default_move_type', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='default_journal_id', kind=None)],
                                keywords=[],
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='default_journal_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='default_move_type', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Attribute(
                                                value=Name(id='journal', ctx=Load()),
                                                attr='type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='sale', kind=None)],
                                        ),
                                        body=Constant(value='out_invoice', kind=None),
                                        orelse=Constant(value='in_invoice', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='default_move_type', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='default_move_type', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='default_move_type', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='move_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
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
                                                            attr='get_invoice_types',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='include_receipts',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='default_move_type', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
                                                        attr='move_type',
                                                        ctx=Load(),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='default_move_type', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='No information about the journal or the type of invoice is passed', kind=None)],
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
                                left=Name(id='default_move_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='entry', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='elements', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//ram:GrandTotalAmount', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='namespaces',
                                        value=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='nsmap',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total_amount', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='elements', ctx=Load()),
                                            Call(
                                                func=Name(id='float', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='elements', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='elements', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//rsm:ExchangedDocument/ram:TypeCode', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='namespaces',
                                        value=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='nsmap',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='type_code', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Name(id='elements', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                attr='text',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='default_move_type', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='_refund', kind=None),
                                    Constant(value='_invoice', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='type_code', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='381', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='default_move_type', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='default_move_type', ctx=Load()),
                                            ops=[Eq()],
                                            comparators=[Constant(value='out_invoice', kind=None)],
                                        ),
                                        body=Constant(value='out_refund', kind=None),
                                        orelse=Constant(value='in_refund', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='refund_sign', ctx=Store())],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='total_amount', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='default_move_type', ctx=Store())],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Name(id='default_move_type', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='out_invoice', kind=None)],
                                                ),
                                                body=Constant(value='out_refund', kind=None),
                                                orelse=Constant(value='in_refund', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='refund_sign', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Constant(value='refund', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='default_move_type', ctx=Load())],
                                        ),
                                        body=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        orelse=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='move_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='default_move_type', ctx=Load()),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='default_move_type',
                                                        value=Name(id='default_move_type', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='account_predictive_bills_disable_prediction',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='invoice_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='partner_type', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='invoice_form', ctx=Load()),
                                                                attr='journal_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='purchase', kind=None)],
                                                    ),
                                                    Constant(value='SellerTradeParty', kind=None),
                                                ],
                                            ),
                                            Constant(value='BuyerTradeParty', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='invoice_form', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_retrieve_partner',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Call(
                                                    func=Name(id='_find_value', ctx=Load()),
                                                    args=[
                                                        JoinedStr(
                                                            values=[
                                                                Constant(value='//ram:', kind=None),
                                                                FormattedValue(
                                                                    value=Name(id='partner_type', ctx=Load()),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value='/ram:Name', kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='mail',
                                                value=Call(
                                                    func=Name(id='_find_value', ctx=Load()),
                                                    args=[
                                                        JoinedStr(
                                                            values=[
                                                                Constant(value='//ram:', kind=None),
                                                                FormattedValue(
                                                                    value=Name(id='partner_type', ctx=Load()),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value="//ram:URIID[@schemeID='SMTP']", kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='vat',
                                                value=Call(
                                                    func=Name(id='_find_value', ctx=Load()),
                                                    args=[
                                                        JoinedStr(
                                                            values=[
                                                                Constant(value='//ram:', kind=None),
                                                                FormattedValue(
                                                                    value=Name(id='partner_type', ctx=Load()),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value='/ram:SpecifiedTaxRegistration/ram:ID', kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//rsm:ExchangedDocument/ram:ID', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='nsmap',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='elements', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='ref',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='elements', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//ram:BuyerOrderReferencedDocument/ram:IssuerAssignedID', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='nsmap',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='elements', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='payment_reference',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='elements', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//ram:IncludedNote/ram:Content', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='nsmap',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='elements', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='narration',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='elements', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//ram:GrandTotalAmount', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='nsmap',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='elements', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='currency_str', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='elements', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='currencyID', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='currency_str', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='currency_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_retrieve_currency',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='currency_str', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='amount_total_import', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='total_amount', ctx=Load()),
                                                        op=Mult(),
                                                        right=Name(id='refund_sign', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//rsm:ExchangedDocument/ram:IssueDateTime/udt:DateTimeString', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='nsmap',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='elements', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='date_str', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='elements', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='date_obj', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='date_str', ctx=Load()),
                                                    Name(id='DEFAULT_FACTURX_DATE_FORMAT', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='invoice_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='date_obj', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//ram:SpecifiedTradePaymentTerms/ram:DueDateDateTime/udt:DateTimeString', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='nsmap',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='elements', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='date_str', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='elements', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='date_obj', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='date_str', ctx=Load()),
                                                    Name(id='DEFAULT_FACTURX_DATE_FORMAT', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='invoice_date_due',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='date_obj', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//ram:IncludedSupplyChainTradeLineItem', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='nsmap',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='elements', ctx=Load()),
                                    body=[
                                        For(
                                            target=Name(id='element', ctx=Store()),
                                            iter=Name(id='elements', ctx=Load()),
                                            body=[
                                                With(
                                                    items=[
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_form', ctx=Load()),
                                                                        attr='invoice_line_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='new',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            optional_vars=Name(id='invoice_line_form', ctx=Store()),
                                                        ),
                                                    ],
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='line_elements', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.//ram:AssociatedDocumentLineDocument/ram:LineID', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='namespaces',
                                                                        value=Attribute(
                                                                            value=Name(id='tree', ctx=Load()),
                                                                            attr='nsmap',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='line_elements', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                            attr='sequence',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Name(id='int', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Name(id='line_elements', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='text',
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
                                                        Assign(
                                                            targets=[Name(id='name', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_find_value', ctx=Load()),
                                                                args=[
                                                                    Constant(value='.//ram:SpecifiedTradeProduct/ram:Name', kind=None),
                                                                    Name(id='element', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='name', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='name', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_retrieve_product',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='default_code',
                                                                        value=Call(
                                                                            func=Name(id='_find_value', ctx=Load()),
                                                                            args=[
                                                                                Constant(value='.//ram:SpecifiedTradeProduct/ram:SellerAssignedID', kind=None),
                                                                                Name(id='element', ctx=Load()),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='name',
                                                                        value=Call(
                                                                            func=Name(id='_find_value', ctx=Load()),
                                                                            args=[
                                                                                Constant(value='.//ram:SpecifiedTradeProduct/ram:Name', kind=None),
                                                                                Name(id='element', ctx=Load()),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='barcode',
                                                                        value=Call(
                                                                            func=Name(id='_find_value', ctx=Load()),
                                                                            args=[
                                                                                Constant(value='.//ram:SpecifiedTradeProduct/ram:GlobalID', kind=None),
                                                                                Name(id='element', ctx=Load()),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='line_elements', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.//ram:SpecifiedLineTradeDelivery/ram:BilledQuantity', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='namespaces',
                                                                        value=Attribute(
                                                                            value=Name(id='tree', ctx=Load()),
                                                                            attr='nsmap',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='line_elements', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                            attr='quantity',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Name(id='float', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Name(id='line_elements', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='text',
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
                                                        Assign(
                                                            targets=[Name(id='line_elements', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.//ram:GrossPriceProductTradePrice/ram:ChargeAmount', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='namespaces',
                                                                        value=Attribute(
                                                                            value=Name(id='tree', ctx=Load()),
                                                                            attr='nsmap',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='line_elements', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='quantity_elements', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//ram:GrossPriceProductTradePrice/ram:BasisQuantity', kind=None)],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='namespaces',
                                                                                value=Attribute(
                                                                                    value=Name(id='tree', ctx=Load()),
                                                                                    attr='nsmap',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='quantity_elements', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                    attr='price_unit',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=BinOp(
                                                                                left=Call(
                                                                                    func=Name(id='float', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Subscript(
                                                                                                value=Name(id='line_elements', ctx=Load()),
                                                                                                slice=Constant(value=0, kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='text',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Div(),
                                                                                right=Call(
                                                                                    func=Name(id='float', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Subscript(
                                                                                                value=Name(id='quantity_elements', ctx=Load()),
                                                                                                slice=Constant(value=0, kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='text',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                    attr='price_unit',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Name(id='float', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='line_elements', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='text',
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
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='line_elements', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//ram:NetPriceProductTradePrice/ram:ChargeAmount', kind=None)],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='namespaces',
                                                                                value=Attribute(
                                                                                    value=Name(id='tree', ctx=Load()),
                                                                                    attr='nsmap',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='line_elements', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='quantity_elements', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='element', ctx=Load()),
                                                                                    attr='xpath',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='.//ram:NetPriceProductTradePrice/ram:BasisQuantity', kind=None)],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='namespaces',
                                                                                        value=Attribute(
                                                                                            value=Name(id='tree', ctx=Load()),
                                                                                            attr='nsmap',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        If(
                                                                            test=Name(id='quantity_elements', ctx=Load()),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[
                                                                                        Attribute(
                                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                                            attr='price_unit',
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                    ],
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Name(id='float', ctx=Load()),
                                                                                            args=[
                                                                                                Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Name(id='line_elements', ctx=Load()),
                                                                                                        slice=Constant(value=0, kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='text',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Div(),
                                                                                        right=Call(
                                                                                            func=Name(id='float', ctx=Load()),
                                                                                            args=[
                                                                                                Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Name(id='quantity_elements', ctx=Load()),
                                                                                                        slice=Constant(value=0, kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='text',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Assign(
                                                                                    targets=[
                                                                                        Attribute(
                                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                                            attr='price_unit',
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                    ],
                                                                                    value=Call(
                                                                                        func=Name(id='float', ctx=Load()),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Name(id='line_elements', ctx=Load()),
                                                                                                    slice=Constant(value=0, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='text',
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
                                                                ),
                                                            ],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='line_elements', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.//ram:AppliedTradeAllowanceCharge/ram:CalculationPercent', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='namespaces',
                                                                        value=Attribute(
                                                                            value=Name(id='tree', ctx=Load()),
                                                                            attr='nsmap',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='line_elements', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                            attr='discount',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Name(id='float', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Name(id='line_elements', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='text',
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
                                                        Assign(
                                                            targets=[Name(id='tax_element', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.//ram:SpecifiedLineTradeSettlement/ram:ApplicableTradeTax/ram:RateApplicablePercent', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='namespaces',
                                                                        value=Attribute(
                                                                            value=Name(id='tree', ctx=Load()),
                                                                            attr='nsmap',
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
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_line_form', ctx=Load()),
                                                                        attr='tax_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='clear',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        For(
                                                            target=Name(id='eline', ctx=Store()),
                                                            iter=Name(id='tax_element', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='tax', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_retrieve_tax',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='amount',
                                                                                value=Attribute(
                                                                                    value=Name(id='eline', ctx=Load()),
                                                                                    attr='text',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='type_tax_use',
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='invoice_form', ctx=Load()),
                                                                                        attr='journal_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='type',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='tax', ctx=Load()),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='invoice_line_form', ctx=Load()),
                                                                                        attr='tax_ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='add',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='tax', ctx=Load())],
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
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Name(id='amount_total_import', ctx=Load()),
                                            body=[
                                                With(
                                                    items=[
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_form', ctx=Load()),
                                                                        attr='invoice_line_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='new',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            optional_vars=Name(id='invoice_line_form', ctx=Store()),
                                                        ),
                                                    ],
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='invoice_form', ctx=Load()),
                                                                        attr='comment',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='/', kind=None),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='quantity',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=1, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='price_unit',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='amount_total_import', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_form', ctx=Load()),
                                    attr='save',
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
