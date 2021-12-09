Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='COUNTRY_EAS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='HU', kind=None),
                    Constant(value='AD', kind=None),
                    Constant(value='AL', kind=None),
                    Constant(value='BA', kind=None),
                    Constant(value='BE', kind=None),
                    Constant(value='BG', kind=None),
                    Constant(value='CH', kind=None),
                    Constant(value='CY', kind=None),
                    Constant(value='CZ', kind=None),
                    Constant(value='DE', kind=None),
                    Constant(value='EE', kind=None),
                    Constant(value='UK', kind=None),
                    Constant(value='GR', kind=None),
                    Constant(value='HR', kind=None),
                    Constant(value='IE', kind=None),
                    Constant(value='LI', kind=None),
                    Constant(value='LT', kind=None),
                    Constant(value='LU', kind=None),
                    Constant(value='LV', kind=None),
                    Constant(value='MC', kind=None),
                    Constant(value='ME', kind=None),
                    Constant(value='MK', kind=None),
                    Constant(value='MT', kind=None),
                    Constant(value='NL', kind=None),
                    Constant(value='PL', kind=None),
                    Constant(value='PT', kind=None),
                    Constant(value='RO', kind=None),
                    Constant(value='RS', kind=None),
                    Constant(value='SI', kind=None),
                    Constant(value='SK', kind=None),
                    Constant(value='SM', kind=None),
                    Constant(value='TR', kind=None),
                    Constant(value='VA', kind=None),
                    Constant(value='SE', kind=None),
                    Constant(value='FR', kind=None),
                ],
                values=[
                    Constant(value=9910, kind=None),
                    Constant(value=9922, kind=None),
                    Constant(value=9923, kind=None),
                    Constant(value=9924, kind=None),
                    Constant(value=9925, kind=None),
                    Constant(value=9926, kind=None),
                    Constant(value=9927, kind=None),
                    Constant(value=9928, kind=None),
                    Constant(value=9929, kind=None),
                    Constant(value=9930, kind=None),
                    Constant(value=9931, kind=None),
                    Constant(value=9932, kind=None),
                    Constant(value=9933, kind=None),
                    Constant(value=9934, kind=None),
                    Constant(value=9935, kind=None),
                    Constant(value=9936, kind=None),
                    Constant(value=9937, kind=None),
                    Constant(value=9938, kind=None),
                    Constant(value=9939, kind=None),
                    Constant(value=9940, kind=None),
                    Constant(value=9941, kind=None),
                    Constant(value=9942, kind=None),
                    Constant(value=9943, kind=None),
                    Constant(value=9944, kind=None),
                    Constant(value=9945, kind=None),
                    Constant(value=9946, kind=None),
                    Constant(value=9947, kind=None),
                    Constant(value=9948, kind=None),
                    Constant(value=9949, kind=None),
                    Constant(value=9950, kind=None),
                    Constant(value=9951, kind=None),
                    Constant(value=9952, kind=None),
                    Constant(value=9953, kind=None),
                    Constant(value=9955, kind=None),
                    Constant(value=9957, kind=None),
                ],
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
                Expr(
                    value=Constant(value=' This edi_format is "abstract" meaning that it provides an additional layer for similar edi_format (formats\n    deriving from EN16931) that share some functionalities but needs to be extended to be used.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='account.edi.format', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_bis3_values',
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
                                    attr='_get_ubl_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='customization_id', kind=None),
                                            Constant(value='profile_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0', kind=None),
                                            Constant(value='urn:fdc:peppol.eu:2017:poacc:billing:01:1.0', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='grouping_key_generator',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='tax_values', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tax', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='tax_values', ctx=Load()),
                                        slice=Constant(value='tax_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='tax_percent', kind=None),
                                            Constant(value='tax_category', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='tax', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                            IfExp(
                                                test=Attribute(
                                                    value=Name(id='tax', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                body=Constant(value='S', kind=None),
                                                orelse=Constant(value='Z', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='tax_details', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='_prepare_edi_tax_details',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='filter_to_apply',
                                        value=Lambda(
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
                                                value=Subscript(
                                                    value=Name(id='x', ctx=Load()),
                                                    slice=Constant(value='tax_repartition_line_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='use_in_tax_closing',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='grouping_key_generator',
                                        value=Name(id='grouping_key_generator', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line_vals', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='values', ctx=Load()),
                                slice=Constant(value='invoice_line_vals_list', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='tax_details', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='invoice_line_tax_details', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Subscript(
                                                            value=Name(id='line_vals', ctx=Load()),
                                                            slice=Constant(value='line', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='tax_details', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[Constant(value='Multiple vat percentage not supported on the same invoice line', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_details_no_tax_closing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='_prepare_edi_tax_details',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='filter_to_apply',
                                        value=Lambda(
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
                                                    value=Subscript(
                                                        value=Name(id='x', ctx=Load()),
                                                        slice=Constant(value='tax_repartition_line_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='use_in_tax_closing',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line_vals', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='values', ctx=Load()),
                                slice=Constant(value='invoice_line_vals_list', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='line_vals', ctx=Load()),
                                            slice=Constant(value='price_subtotal_with_no_tax_closing', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Name(id='line_vals', ctx=Load()),
                                            slice=Constant(value='line', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='price_subtotal',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='tax_detail', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='tax_details_no_tax_closing', ctx=Load()),
                                                        slice=Constant(value='invoice_line_tax_details', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Subscript(
                                                        value=Name(id='line_vals', ctx=Load()),
                                                        slice=Constant(value='line', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='tax_details', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='line_vals', ctx=Load()),
                                                slice=Constant(value='price_subtotal_with_no_tax_closing', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Subscript(
                                                value=Name(id='tax_detail', ctx=Load()),
                                                slice=Constant(value='tax_amount_currency', kind=None),
                                                ctx=Load(),
                                            ),
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
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='total_untaxed_amount', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='x', ctx=Load()),
                                            slice=Constant(value='price_subtotal_with_no_tax_closing', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='invoice_line_vals_list', kind=None),
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
                        For(
                            target=Name(id='partner_vals', ctx=Store()),
                            iter=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='customer_vals', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='supplier_vals', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='partner_vals', ctx=Load()),
                                        slice=Constant(value='partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='COUNTRY_EAS', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='partner_vals', ctx=Load()),
                                                    slice=Constant(value='bis3_endpoint', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='partner_vals', ctx=Load()),
                                                    slice=Constant(value='bis3_endpoint_scheme', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='COUNTRY_EAS', ctx=Load()),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
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
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_bis3_namespaces',
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='cac', kind=None),
                                    Constant(value='cbc', kind=None),
                                ],
                                values=[
                                    Constant(value='urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2', kind=None),
                                    Constant(value='urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_bis3_get_extra_partner_domains',
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
                        Expr(
                            value=Constant(value=' Returns an additional domain to find the partner of the invoice based on specific implementation of BIS3.\n        TO OVERRIDE\n\n        :returns: a list of domains\n        ', kind=None),
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_decode_bis3',
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
                            value=Constant(value=' Decodes an EN16931 invoice into an invoice.\n        :param tree:    the UBL (EN16931) tree to decode.\n        :param invoice: the invoice to update or an empty recordset.\n        :returns:       the invoice where the UBL (EN16931) data was imported.\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='_find_value',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='path', annotation=None, type_comment=None),
                                    arg(arg='root', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Name(id='tree', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='element', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='root', ctx=Load()),
                                            attr='find',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='element', ctx=Load()),
                                            ops=[IsNot()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        body=Attribute(
                                            value=Name(id='element', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=None, kind=None),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
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
                                args=[Constant(value='./{*}InvoiceTypeCode', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='element', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='type_code', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='element', ctx=Load()),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move_type', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='type_code', ctx=Load()),
                                            ops=[Eq()],
                                            comparators=[Constant(value='381', kind=None)],
                                        ),
                                        body=Constant(value='in_refund', kind=None),
                                        orelse=Constant(value='in_invoice', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='move_type', ctx=Store())],
                                    value=Constant(value='in_invoice', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='default_journal', ctx=Store())],
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
                                                arg='default_move_type',
                                                value=Name(id='move_type', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='_get_default_journal',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                                        value=Name(id='move_type', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='default_journal_id',
                                                        value=Attribute(
                                                            value=Name(id='default_journal', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
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
                                    targets=[Name(id='element', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='find',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='./{*}ID', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='element', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
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
                                                value=Name(id='element', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='element', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='find',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='./{*}IssueDate', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='element', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
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
                                                value=Name(id='element', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='element', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='find',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='./{*}DueDate', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='element', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
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
                                                value=Name(id='element', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                                                args=[Constant(value='./{*}DocumentCurrencyCode', kind=None)],
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
                                    targets=[Name(id='specific_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_bis3_get_extra_partner_domains',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tree', ctx=Load())],
                                        keywords=[],
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
                                                    args=[Constant(value='./{*}AccountingSupplierParty/{*}Party/*/{*}Name', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='phone',
                                                value=Call(
                                                    func=Name(id='_find_value', ctx=Load()),
                                                    args=[Constant(value='./{*}AccountingSupplierParty/{*}Party/*/{*}Telephone', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='mail',
                                                value=Call(
                                                    func=Name(id='_find_value', ctx=Load()),
                                                    args=[Constant(value='./{*}AccountingSupplierParty/{*}Party/*/{*}ElectronicMail', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='vat',
                                                value=Call(
                                                    func=Name(id='_find_value', ctx=Load()),
                                                    args=[Constant(value='./{*}AccountingSupplierParty/{*}Party/{*}PartyTaxScheme/{*}CompanyID', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='domain',
                                                value=Name(id='specific_domain', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='eline', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='findall',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.//{*}InvoiceLine', kind=None)],
                                        keywords=[],
                                    ),
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
                                                                        Constant(value='./{*}Item/{*}SellersItemIdentification/{*}ID', kind=None),
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
                                                                        Constant(value='./{*}Item/{*}Name', kind=None),
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
                                                                        Constant(value="./{*}Item/{*}StandardItemIdentification/{*}ID[@schemeID='0160']", kind=None),
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
                                                    targets=[Name(id='element', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='eline', ctx=Load()),
                                                            attr='find',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='./{*}InvoicedQuantity', kind=None)],
                                                        keywords=[],
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
                                                                    Compare(
                                                                        left=Name(id='element', ctx=Load()),
                                                                        ops=[IsNot()],
                                                                        comparators=[Constant(value=None, kind=None)],
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='float', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='element', ctx=Load()),
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
                                                    targets=[Name(id='element', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='eline', ctx=Load()),
                                                            attr='find',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='./{*}Price/{*}PriceAmount', kind=None)],
                                                        keywords=[],
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
                                                                    Compare(
                                                                        left=Name(id='element', ctx=Load()),
                                                                        ops=[IsNot()],
                                                                        comparators=[Constant(value=None, kind=None)],
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='float', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='element', ctx=Load()),
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
                                                    targets=[Name(id='line_extension_amount', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='element', ctx=Load()),
                                                                        ops=[IsNot()],
                                                                        comparators=[Constant(value=None, kind=None)],
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='float', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='element', ctx=Load()),
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
                                                    targets=[Name(id='element', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='eline', ctx=Load()),
                                                            attr='find',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='./{*}Item/{*}Description', kind=None)],
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
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='element', ctx=Load()),
                                                                        ops=[IsNot()],
                                                                        comparators=[Constant(value=None, kind=None)],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='element', ctx=Load()),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='tax_elements', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='eline', ctx=Load()),
                                                            attr='findall',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='./{*}Item/{*}ClassifiedTaxCategory', kind=None)],
                                                        keywords=[],
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
                                                    target=Name(id='tax_element', ctx=Store()),
                                                    iter=Name(id='tax_elements', ctx=Load()),
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
                                                                args=[
                                                                    Call(
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
                                                                                        Constant(value='./{*}Percent', kind=None),
                                                                                        Name(id='tax_element', ctx=Load()),
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
                                                                ],
                                                                keywords=[],
                                                            ),
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
