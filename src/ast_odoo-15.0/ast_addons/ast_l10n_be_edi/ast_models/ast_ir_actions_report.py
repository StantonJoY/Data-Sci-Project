Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='xml.sax.saxutils',
            names=[
                alias(name='escape', asname=None),
                alias(name='quoteattr', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='IrActionsReport',
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
                    value=Constant(value='ir.actions.report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_postprocess_pdf_report',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='buffer', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Add the pdf report in the e-fff XML as base64 string.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_postprocess_pdf_report',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='buffer', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='_name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='account.move', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='edi_attachment', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='edi_document_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='d', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='d', ctx=Load()),
                                                                attr='edi_format_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='efff_1', kind=None)],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='attachment_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='edi_attachment', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='old_xml', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64decode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='edi_attachment', ctx=Load()),
                                                                attr='with_context',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='bin_size',
                                                                    value=Constant(value=False, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                        attr='datas',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='validate',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='tree', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='fromstring',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='old_xml', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='document_currency_code_elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value="//*[local-name()='DocumentCurrencyCode']", kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='additional_document_elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value="//*[local-name()='AdditionalDocumentReference']", kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='document_currency_code_elements', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='additional_document_elements', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='pdf', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='base64', ctx=Load()),
                                                                    attr='b64encode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='buffer', ctx=Load()),
                                                                            attr='getvalue',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='pdf_name', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='%s.pdf', kind=None),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='_get_efff_name',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='to_inject', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='\n                        <cac:AdditionalDocumentReference\n                            xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"\n                            xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"\n                            xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2">\n                            <cbc:ID>%s</cbc:ID>\n                            <cac:Attachment>\n                                <cbc:EmbeddedDocumentBinaryObject mimeCode="application/pdf" filename=%s>\n                                    %s\n                                </cbc:EmbeddedDocumentBinaryObject>\n                            </cac:Attachment>\n                        </cac:AdditionalDocumentReference>\n                    ', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Name(id='escape', ctx=Load()),
                                                                    args=[Name(id='pdf_name', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Name(id='quoteattr', ctx=Load()),
                                                                    args=[Name(id='pdf_name', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Name(id='pdf', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='document_currency_code_elements', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='addnext',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='etree', ctx=Load()),
                                                                    attr='fromstring',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='to_inject', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='new_xml', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='etree', ctx=Load()),
                                                            attr='tostring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='tree', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='pretty_print',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='edi_attachment', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='res_model', kind=None),
                                                                    Constant(value='res_id', kind=None),
                                                                    Constant(value='datas', kind=None),
                                                                    Constant(value='mimetype', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='account.move', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='base64', ctx=Load()),
                                                                            attr='b64encode',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='new_xml', ctx=Load())],
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
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
