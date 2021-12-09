Module(
    body=[
        ImportFrom(
            module='PyPDF2',
            names=[
                alias(name='PdfFileWriter', asname=None),
                alias(name='PdfFileReader', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='PyPDF2.generic',
            names=[
                alias(name='DictionaryObject', asname=None),
                alias(name='DecodedStreamObject', asname=None),
                alias(name='NameObject', asname=None),
                alias(name='createStringObject', asname=None),
                alias(name='ArrayObject', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='PyPDF2.utils',
            names=[alias(name='b_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        Assign(
            targets=[Name(id='DEFAULT_PDF_DATETIME_FORMAT', ctx=Store())],
            value=Constant(value="D:%Y%m%d%H%M%S+00'00'", kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='_unwrapping_get',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='key', annotation=None, type_comment=None),
                    arg(arg='default', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Try(
                    body=[
                        Return(
                            value=Subscript(
                                value=Name(id='self', ctx=Load()),
                                slice=Name(id='key', ctx=Load()),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='KeyError', ctx=Load()),
                            name=None,
                            body=[
                                Return(
                                    value=Name(id='default', ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='DictionaryObject', ctx=Load()),
                    attr='get',
                    ctx=Store(),
                ),
            ],
            value=Name(id='_unwrapping_get', ctx=Load()),
            type_comment=None,
        ),
        ClassDef(
            name='BrandedFileWriter',
            bases=[Name(id='PdfFileWriter', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='addMetadata',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='/Creator', kind=None),
                                            Constant(value='/Producer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Odoo', kind=None),
                                            Constant(value='Odoo', kind=None),
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
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='PdfFileWriter', ctx=Store())],
            value=Name(id='BrandedFileWriter', ctx=Load()),
            type_comment=None,
        ),
        FunctionDef(
            name='merge_pdf',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='pdf_data', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Merge a collection of PDF documents in one.\n    Note that the attachments are not merged.\n    :param list pdf_data: a list of PDF datastrings\n    :return: a unique merged PDF datastring\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='writer', ctx=Store())],
                    value=Call(
                        func=Name(id='PdfFileWriter', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='document', ctx=Store()),
                    iter=Name(id='pdf_data', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='reader', ctx=Store())],
                            value=Call(
                                func=Name(id='PdfFileReader', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='document', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='strict',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='page', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='reader', ctx=Load()),
                                            attr='getNumPages',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='addPage',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='reader', ctx=Load()),
                                                    attr='getPage',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='page', ctx=Load())],
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
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=Name(id='_buffer', ctx=Store()),
                        ),
                    ],
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='_buffer', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_buffer', ctx=Load()),
                                    attr='getvalue',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='rotate_pdf',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='pdf', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Rotate clockwise PDF (90°) into a new PDF.\n    Note that the attachments are not copied.\n    :param pdf: a PDF to rotate\n    :return: a PDF rotated\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='writer', ctx=Store())],
                    value=Call(
                        func=Name(id='PdfFileWriter', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reader', ctx=Store())],
                    value=Call(
                        func=Name(id='PdfFileReader', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[Name(id='pdf', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='strict',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='page', ctx=Store()),
                    iter=Call(
                        func=Name(id='range', ctx=Load()),
                        args=[
                            Constant(value=0, kind=None),
                            Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='getNumPages',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='page', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='getPage',
                                    ctx=Load(),
                                ),
                                args=[Name(id='page', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='page', ctx=Load()),
                                    attr='rotateClockwise',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=90, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='addPage',
                                    ctx=Load(),
                                ),
                                args=[Name(id='page', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=Name(id='_buffer', ctx=Store()),
                        ),
                    ],
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='_buffer', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_buffer', ctx=Load()),
                                    attr='getvalue',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='old_init', ctx=Store())],
            value=Attribute(
                value=Name(id='PdfFileReader', ctx=Load()),
                attr='__init__',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='PdfFileReader', ctx=Load()),
                    attr='__init__',
                    ctx=Store(),
                ),
            ],
            value=Lambda(
                args=arguments(
                    posonlyargs=[],
                    args=[
                        arg(arg='self', annotation=None, type_comment=None),
                        arg(arg='stream', annotation=None, type_comment=None),
                        arg(arg='strict', annotation=None, type_comment=None),
                        arg(arg='warndest', annotation=None, type_comment=None),
                        arg(arg='overwriteWarnings', annotation=None, type_comment=None),
                    ],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[
                        Constant(value=True, kind=None),
                        Constant(value=None, kind=None),
                        Constant(value=True, kind=None),
                    ],
                ),
                body=Call(
                    func=Name(id='old_init', ctx=Load()),
                    args=[Name(id='self', ctx=Load())],
                    keywords=[
                        keyword(
                            arg='stream',
                            value=Name(id='stream', ctx=Load()),
                        ),
                        keyword(
                            arg='strict',
                            value=Name(id='strict', ctx=Load()),
                        ),
                        keyword(
                            arg='warndest',
                            value=Constant(value=None, kind=None),
                        ),
                        keyword(
                            arg='overwriteWarnings',
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                ),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='OdooPdfFileReader',
            bases=[Name(id='PdfFileReader', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Returns the files inside the PDF.\n    :raises NotImplementedError: if document is encrypted and uses an unsupported encryption method.\n    ', kind=None),
                ),
                FunctionDef(
                    name='getAttachments',
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='isEncrypted',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='decrypt',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='file_path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='trailer',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='/Root', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='/Names', kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='/EmbeddedFiles', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/Names', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=List(elts=[], ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='file_path', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='file_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='file_path', ctx=Load()),
                                                slice=BinOp(
                                                    left=Name(id='i', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='getObject',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(
                                        value=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    slice=Constant(value='/F', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='attachment', ctx=Load()),
                                                                        slice=Constant(value='/EF', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='/F', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='getObject',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='getData',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='OdooPdfFileWriter',
            bases=[Name(id='PdfFileWriter', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_create_attachment_object',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attachment', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create a PyPdf2.generic object representing an embedded file.\n\n        :param attachment: A dictionary containing:\n            * filename: The name of the file to embed (require).\n            * content:  The content of the file encoded in base64 (require).\n        :return:\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='file_entry', ctx=Store())],
                            value=Call(
                                func=Name(id='DecodedStreamObject', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='file_entry', ctx=Load()),
                                    attr='setData',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='attachment', ctx=Load()),
                                        slice=Constant(value='content', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='file_entry', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/Type', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/Params', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/EmbeddedFile', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='DictionaryObject', ctx=Load()),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Call(
                                                                func=Name(id='NameObject', ctx=Load()),
                                                                args=[Constant(value='/CheckSum', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='NameObject', ctx=Load()),
                                                                args=[Constant(value='/ModDate', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='NameObject', ctx=Load()),
                                                                args=[Constant(value='/Size', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='createStringObject', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='hashlib', ctx=Load()),
                                                                                    attr='md5',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='attachment', ctx=Load()),
                                                                                        slice=Constant(value='content', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='hexdigest',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='createStringObject', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='datetime', ctx=Load()),
                                                                                    attr='now',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='strftime',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='DEFAULT_PDF_DATETIME_FORMAT', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='NameObject', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='len', ctx=Load()),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='attachment', ctx=Load()),
                                                                                        slice=Constant(value='content', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='subtype', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='file_entry', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Call(
                                                        func=Name(id='NameObject', ctx=Load()),
                                                        args=[Constant(value='/Subtype', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='NameObject', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='attachment', ctx=Load()),
                                                                slice=Constant(value='subtype', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
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
                        Assign(
                            targets=[Name(id='file_entry_object', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_addObject',
                                    ctx=Load(),
                                ),
                                args=[Name(id='file_entry', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filename_object', ctx=Store())],
                            value=Call(
                                func=Name(id='createStringObject', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='attachment', ctx=Load()),
                                        slice=Constant(value='filename', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filespec_object', ctx=Store())],
                            value=Call(
                                func=Name(id='DictionaryObject', ctx=Load()),
                                args=[
                                    Dict(
                                        keys=[
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/AFRelationship', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/Type', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/F', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/EF', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/UF', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/Data', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='NameObject', ctx=Load()),
                                                args=[Constant(value='/Filespec', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='filename_object', ctx=Load()),
                                            Call(
                                                func=Name(id='DictionaryObject', ctx=Load()),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Call(
                                                                func=Name(id='NameObject', ctx=Load()),
                                                                args=[Constant(value='/F', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='NameObject', ctx=Load()),
                                                                args=[Constant(value='/UF', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        values=[
                                                            Name(id='file_entry_object', ctx=Load()),
                                                            Name(id='file_entry_object', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='filename_object', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='description', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='filespec_object', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Call(
                                                        func=Name(id='NameObject', ctx=Load()),
                                                        args=[Constant(value='/Desc', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='createStringObject', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='attachment', ctx=Load()),
                                                                slice=Constant(value='description', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_addObject',
                                    ctx=Load(),
                                ),
                                args=[Name(id='filespec_object', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='addAttachment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fname', annotation=None, type_comment=None),
                            arg(arg='fdata', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_root_object',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/Names', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_root_object',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='/Names', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/EmbeddedFiles', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='attachments', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_root_object',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='/Names', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='/EmbeddedFiles', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='/Names', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_create_attachment_object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='filename', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Name(id='fname', ctx=Load()),
                                                    Name(id='fdata', ctx=Load()),
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
                                            value=Name(id='attachments', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='new_attachment', ctx=Load()),
                                                                attr='getObject',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value='/F', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='new_attachment', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='addAttachment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fname', ctx=Load()),
                                            Name(id='fdata', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
