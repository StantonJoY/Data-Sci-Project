Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_repr', asname=None),
                alias(name='html2plaintext', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='pathlib',
            names=[alias(name='PureWindowsPath', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='markupsafe', asname=None)],
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
                    name='_is_ubl',
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
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='tag',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='{urn:oasis:names:specification:ubl:schema:xsd:Invoice-2}Invoice', kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice_from_ubl',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='journal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='_get_default_journal',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_type', ctx=Store())],
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
                        Assign(
                            targets=[Name(id='element', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='find',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='.//{*}InvoiceTypeCode', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='element', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='element', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='381', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='move_type', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='move_type', ctx=Load()),
                                            ops=[Eq()],
                                            comparators=[Constant(value='in_invoice', kind=None)],
                                        ),
                                        body=Constant(value='in_refund', kind=None),
                                        orelse=Constant(value='out_refund', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default_move_type',
                                        value=Name(id='move_type', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='default_journal_id',
                                        value=Attribute(
                                            value=Name(id='journal', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_import_ubl',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_invoice_from_ubl',
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
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default_move_type',
                                        value=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='move_type',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='default_journal_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_import_ubl',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_import_ubl',
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
                            value=Constant(value=' Decodes an UBL invoice into an invoice.\n\n        :param tree:    the UBL tree to decode.\n        :param invoice: the invoice to update or an empty recordset.\n        :returns:       the invoice where the UBL data was imported.\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='_get_ubl_namespaces',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Constant(value=" If the namespace is declared with xmlns='...', the namespaces map contains the 'None' key that causes an\n            TypeError: empty namespace prefix is not supported in XPath\n            Then, we need to remap arbitrarily this key.\n\n            :param tree: An instance of etree.\n            :return: The namespaces map without 'None' key.\n            ", kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='namespaces', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='tree', ctx=Load()),
                                        attr='nsmap',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='namespaces', ctx=Load()),
                                            slice=Constant(value='inv', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='namespaces', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=None, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='namespaces', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='namespaces', ctx=Store())],
                            value=Call(
                                func=Name(id='_get_ubl_namespaces', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                            Name(id='namespaces', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
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
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//cbc:ID', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='namespaces', ctx=Load()),
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
                                        args=[Constant(value='//cbc:InstructionID', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='namespaces', ctx=Load()),
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
                                        args=[Constant(value='//cbc:IssueDate', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='namespaces', ctx=Load()),
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
                                                    attr='invoice_date',
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
                                        args=[Constant(value='//cbc:PaymentDueDate', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='namespaces', ctx=Load()),
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
                                                    attr='invoice_date_due',
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
                                        args=[Constant(value='//cbc:DueDate', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='namespaces', ctx=Load()),
                                            ),
                                        ],
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
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='invoice_form', ctx=Load()),
                                                attr='invoice_date_due',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='elements', ctx=Load()),
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
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='currency', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_retrieve_currency',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_find_value', ctx=Load()),
                                                args=[Constant(value='//cbc:DocumentCurrencyCode', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='currency', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='currency', ctx=Load()),
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
                                        args=[Constant(value='//cbc:TransportExecutionTerms/cac:DeliveryTerms/cbc:ID', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='namespaces', ctx=Load()),
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
                                                    attr='invoice_incoterm_id',
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
                                                        slice=Constant(value='account.incoterms', kind=None),
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
                                                                    Constant(value='code', kind=None),
                                                                    Constant(value='=', kind=None),
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
                                    ],
                                    orelse=[],
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
                                                    args=[Constant(value='//cac:AccountingSupplierParty/cac:Party//cbc:Name', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='phone',
                                                value=Call(
                                                    func=Name(id='_find_value', ctx=Load()),
                                                    args=[Constant(value='//cac:AccountingSupplierParty/cac:Party//cbc:Telephone', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='mail',
                                                value=Call(
                                                    func=Name(id='_find_value', ctx=Load()),
                                                    args=[Constant(value='//cac:AccountingSupplierParty/cac:Party//cbc:ElectronicMail', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='vat',
                                                value=Call(
                                                    func=Name(id='_find_value', ctx=Load()),
                                                    args=[Constant(value='//cac:AccountingSupplierParty/cac:Party//cbc:CompanyID', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='lines_elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//cac:InvoiceLine', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='namespaces', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='eline', ctx=Store()),
                                    iter=Name(id='lines_elements', ctx=Load()),
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
                                                                        Constant(value='cac:Item/cac:SellersItemIdentification/cbc:ID', kind=None),
                                                                        Name(id='eline', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='name',
                                                                value=Call(
                                                                    func=Name(id='_find_value', ctx=Load()),
                                                                    args=[
                                                                        Constant(value='cac:Item/cbc:Name', kind=None),
                                                                        Name(id='eline', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='barcode',
                                                                value=Call(
                                                                    func=Name(id='_find_value', ctx=Load()),
                                                                    args=[
                                                                        Constant(value="cac:Item/cac:StandardItemIdentification/cbc:ID[@schemeID='0160']", kind=None),
                                                                        Name(id='eline', ctx=Load()),
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
                                                            value=Name(id='eline', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='cbc:InvoicedQuantity', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='namespaces',
                                                                value=Name(id='namespaces', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='quantity', ctx=Store())],
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
                                                            Constant(value=1.0, kind=None),
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
                                                    value=Name(id='quantity', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='elements', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='eline', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='cac:Price/cbc:PriceAmount', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='namespaces',
                                                                value=Name(id='namespaces', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='price_unit', ctx=Store())],
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
                                                            value=Name(id='eline', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='cbc:LineExtensionAmount', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='namespaces',
                                                                value=Name(id='namespaces', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='line_extension_amount', ctx=Store())],
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
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                            attr='price_unit',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='price_unit', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='line_extension_amount', ctx=Load()),
                                                                op=Div(),
                                                                right=Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='quantity',
                                                                    ctx=Load(),
                                                                ),
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
                                                            value=Name(id='eline', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='cac:Item/cbc:Description', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='namespaces',
                                                                value=Name(id='namespaces', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='elements', ctx=Load()),
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
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='name',
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
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_line_form', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='%month%', kind=None),
                                                                    Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='fields', ctx=Load()),
                                                                                            attr='Date',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='to_date',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='invoice_form', ctx=Load()),
                                                                                            attr='invoice_date',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='month',
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
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_line_form', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='%year%', kind=None),
                                                                    Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='fields', ctx=Load()),
                                                                                            attr='Date',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='to_date',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='invoice_form', ctx=Load()),
                                                                                            attr='invoice_date',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='year',
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
                                                            targets=[Name(id='partner_name', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_find_value', ctx=Load()),
                                                                args=[Constant(value='//cac:AccountingSupplierParty/cac:Party//cbc:Name', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BinOp(
                                                                left=Constant(value='%s (%s)', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Name(id='partner_name', ctx=Load()),
                                                                                Constant(value='', kind=None),
                                                                            ],
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='invoice_form', ctx=Load()),
                                                                            attr='invoice_date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                Assign(
                                                    targets=[Name(id='tax_element', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='eline', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='cac:TaxTotal/cac:TaxSubtotal', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='namespaces',
                                                                value=Name(id='namespaces', ctx=Load()),
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
                                                                        value=Call(
                                                                            func=Name(id='_find_value', ctx=Load()),
                                                                            args=[
                                                                                Constant(value='cbc:Percent', kind=None),
                                                                                Name(id='eline', ctx=Load()),
                                                                            ],
                                                                            keywords=[],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachments', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.attachment', kind=None),
                                ctx=Load(),
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
                                args=[Constant(value='//cac:AdditionalDocumentReference', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='namespaces',
                                        value=Name(id='namespaces', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='element', ctx=Store()),
                            iter=Name(id='elements', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='attachment_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='element', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='cbc:ID', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='namespaces', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attachment_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='element', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='cac:Attachment//cbc:EmbeddedDocumentBinaryObject', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='namespaces',
                                                value=Name(id='namespaces', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='attachment_name', ctx=Load()),
                                            Name(id='attachment_data', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='text', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='attachment_data', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Call(
                                                        func=Name(id='PureWindowsPath', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='attachment_name', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='stem',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='.pdf', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='attachments', ctx=Store()),
                                            op=BitOr(),
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
                                                            Constant(value='res_id', kind=None),
                                                            Constant(value='res_model', kind=None),
                                                            Constant(value='datas', kind=None),
                                                            Constant(value='type', kind=None),
                                                            Constant(value='mimetype', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='name', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='account.move', kind=None),
                                                            BinOp(
                                                                left=Name(id='text', ctx=Load()),
                                                                op=Add(),
                                                                right=BinOp(
                                                                    left=Constant(value='=', kind=None),
                                                                    op=Mult(),
                                                                    right=BinOp(
                                                                        left=Call(
                                                                            func=Name(id='len', ctx=Load()),
                                                                            args=[Name(id='text', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Mod(),
                                                                        right=Constant(value=3, kind=None),
                                                                    ),
                                                                ),
                                                            ),
                                                            Constant(value='binary', kind=None),
                                                            Constant(value='application/pdf', kind=None),
                                                        ],
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
                            test=Name(id='attachments', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='no_new_invoice',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='attachment_ids',
                                                value=Attribute(
                                                    value=Name(id='attachments', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='invoice', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_ubl_values',
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
                        Expr(
                            value=Constant(value=' Get the necessary values to generate the XML. These values will be used in the qweb template when\n        rendering. Needed values differ depending on the implementation of the UBL, as (sub)template can be overriden\n        or called dynamically.\n        :returns:   a dictionary with the value used in the template has key and the value as value.\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='format_monetary',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='amount', annotation=None, type_comment=None)],
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
                                            Name(id='amount', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
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
                        Return(
                            value=Dict(
                                keys=[
                                    None,
                                    Constant(value='tax_details', kind=None),
                                    Constant(value='ubl_version', kind=None),
                                    Constant(value='type_code', kind=None),
                                    Constant(value='payment_means_code', kind=None),
                                    Constant(value='bank_account', kind=None),
                                    Constant(value='note', kind=None),
                                    Constant(value='format_monetary', kind=None),
                                    Constant(value='customer_vals', kind=None),
                                    Constant(value='supplier_vals', kind=None),
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
                                    Constant(value=2.1, kind=None),
                                    IfExp(
                                        test=Compare(
                                            left=Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='move_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='out_invoice', kind=None)],
                                        ),
                                        body=Constant(value=380, kind=None),
                                        orelse=Constant(value=381, kind=None),
                                    ),
                                    IfExp(
                                        test=Attribute(
                                            value=Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='journal_id',
                                                ctx=Load(),
                                            ),
                                            attr='bank_account_id',
                                            ctx=Load(),
                                        ),
                                        body=Constant(value=42, kind=None),
                                        orelse=Constant(value=31, kind=None),
                                    ),
                                    Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='partner_bank_id',
                                        ctx=Load(),
                                    ),
                                    IfExp(
                                        test=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='narration',
                                            ctx=Load(),
                                        ),
                                        body=Call(
                                            func=Name(id='html2plaintext', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='narration',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    Name(id='format_monetary', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='partner', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='commercial_partner_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[Constant(value='partner', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='commercial_partner_id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='_export_ubl',
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
                                        args=[Constant(value='account_edi_ubl.export_ubl_invoice', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_ubl_values',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoice', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml_name', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s_ubl_2_1.xml', kind=None),
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
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
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
                                            Constant(value='account.move', kind=None),
                                            Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='ubl_2_1', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_ubl',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='filename', ctx=Load()),
                                            Name(id='tree', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_create_invoice_from_ubl',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tree', ctx=Load())],
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='ubl_2_1', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_ubl',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='filename', ctx=Load()),
                                            Name(id='tree', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_update_invoice_from_ubl',
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
                    name='_is_compatible_with_journal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='journal', annotation=None, type_comment=None),
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
                                comparators=[Constant(value='ubl_2_1', kind=None)],
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
                                            attr='_is_compatible_with_journal',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='journal', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='journal', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='sale', kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_enabled_by_default_on_journal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='journal', annotation=None, type_comment=None),
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
                                comparators=[Constant(value='ubl_2_1', kind=None)],
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
                                            attr='_is_enabled_by_default_on_journal',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='journal', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
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
                                comparators=[Constant(value='ubl_2_1', kind=None)],
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
                                            attr='_export_ubl',
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
