Module(
    body=[
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='xml.dom.minidom', asname=None)],
        ),
        Import(
            names=[alias(name='zipfile', asname=None)],
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
        Try(
            body=[
                ImportFrom(
                    module='pdfminer.pdfinterp',
                    names=[
                        alias(name='PDFResourceManager', asname=None),
                        alias(name='PDFPageInterpreter', asname=None),
                    ],
                    level=0,
                ),
                ImportFrom(
                    module='pdfminer.converter',
                    names=[alias(name='TextConverter', asname=None)],
                    level=0,
                ),
                ImportFrom(
                    module='pdfminer.pdfpage',
                    names=[alias(name='PDFPage', asname=None)],
                    level=0,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[
                                Name(id='PDFResourceManager', ctx=Store()),
                                Name(id='PDFPageInterpreter', ctx=Store()),
                                Name(id='TextConverter', ctx=Store()),
                                Name(id='PDFPage', ctx=Store()),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="Attachment indexation of PDF documents is unavailable because the 'pdfminer' Python library cannot be found on the system. You may install it from https://pypi.org/project/pdfminer.six/ (e.g. `pip3 install pdfminer.six`)", kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Assign(
            targets=[Name(id='FTYPES', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='docx', kind=None),
                    Constant(value='pptx', kind=None),
                    Constant(value='xlsx', kind=None),
                    Constant(value='opendoc', kind=None),
                    Constant(value='pdf', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='textToString',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='element', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='buff', ctx=Store())],
                    value=Constant(value='', kind='u'),
                    type_comment=None,
                ),
                For(
                    target=Name(id='node', ctx=Store()),
                    iter=Attribute(
                        value=Name(id='element', ctx=Load()),
                        attr='childNodes',
                        ctx=Load(),
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='nodeType',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='xml', ctx=Load()),
                                                attr='dom',
                                                ctx=Load(),
                                            ),
                                            attr='Node',
                                            ctx=Load(),
                                        ),
                                        attr='TEXT_NODE',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='buff', ctx=Store()),
                                    op=Add(),
                                    value=Attribute(
                                        value=Name(id='node', ctx=Load()),
                                        attr='nodeValue',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='nodeType',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='xml', ctx=Load()),
                                                        attr='dom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='Node',
                                                    ctx=Load(),
                                                ),
                                                attr='ELEMENT_NODE',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='buff', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='textToString', ctx=Load()),
                                                args=[Name(id='node', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='buff', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='IrAttachment',
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
                    value=Constant(value='ir.attachment', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_index_docx',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Index Microsoft .docx documents', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='buf', ctx=Store())],
                            value=Constant(value='', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bin_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='zipfile', ctx=Load()),
                                    attr='is_zipfile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='f', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='zf', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='zipfile', ctx=Load()),
                                                    attr='ZipFile',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='f', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='xml', ctx=Load()),
                                                            attr='dom',
                                                            ctx=Load(),
                                                        ),
                                                        attr='minidom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='parseString',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='zf', ctx=Load()),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='word/document.xml', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='val', ctx=Store()),
                                            iter=List(
                                                elts=[
                                                    Constant(value='w:p', kind=None),
                                                    Constant(value='w:h', kind=None),
                                                    Constant(value='text:list', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='element', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='content', ctx=Load()),
                                                            attr='getElementsByTagName',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='val', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='buf', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Name(id='textToString', ctx=Load()),
                                                                    args=[Name(id='element', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value='\n', kind=None),
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
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='buf', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_index_pptx',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Index Microsoft .pptx documents', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='buf', ctx=Store())],
                            value=Constant(value='', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bin_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='zipfile', ctx=Load()),
                                    attr='is_zipfile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='f', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='zf', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='zipfile', ctx=Load()),
                                                    attr='ZipFile',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='f', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='zf_filelist', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='x', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='zf', ctx=Load()),
                                                                attr='namelist',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='startswith',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='ppt/slides/slide', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='i', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[
                                                    Constant(value=1, kind=None),
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='zf_filelist', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='content', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='xml', ctx=Load()),
                                                                    attr='dom',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='minidom',
                                                                ctx=Load(),
                                                            ),
                                                            attr='parseString',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='zf', ctx=Load()),
                                                                    attr='read',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='ppt/slides/slide%s.xml', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='i', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='val', ctx=Store()),
                                                    iter=List(
                                                        elts=[Constant(value='a:t', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        For(
                                                            target=Name(id='element', ctx=Store()),
                                                            iter=Call(
                                                                func=Attribute(
                                                                    value=Name(id='content', ctx=Load()),
                                                                    attr='getElementsByTagName',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='val', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='buf', ctx=Store()),
                                                                    op=Add(),
                                                                    value=BinOp(
                                                                        left=Call(
                                                                            func=Name(id='textToString', ctx=Load()),
                                                                            args=[Name(id='element', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value='\n', kind=None),
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
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='buf', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_index_xlsx',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Index Microsoft .xlsx documents', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='buf', ctx=Store())],
                            value=Constant(value='', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bin_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='zipfile', ctx=Load()),
                                    attr='is_zipfile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='f', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='zf', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='zipfile', ctx=Load()),
                                                    attr='ZipFile',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='f', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='xml', ctx=Load()),
                                                            attr='dom',
                                                            ctx=Load(),
                                                        ),
                                                        attr='minidom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='parseString',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='zf', ctx=Load()),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='xl/sharedStrings.xml', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='val', ctx=Store()),
                                            iter=List(
                                                elts=[Constant(value='t', kind=None)],
                                                ctx=Load(),
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='element', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='content', ctx=Load()),
                                                            attr='getElementsByTagName',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='val', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='buf', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Name(id='textToString', ctx=Load()),
                                                                    args=[Name(id='element', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value='\n', kind=None),
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
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='buf', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_index_opendoc',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Index OpenDocument documents (.odt, .ods...)', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='buf', ctx=Store())],
                            value=Constant(value='', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bin_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='zipfile', ctx=Load()),
                                    attr='is_zipfile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='f', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='zf', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='zipfile', ctx=Load()),
                                                    attr='ZipFile',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='f', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='xml', ctx=Load()),
                                                            attr='dom',
                                                            ctx=Load(),
                                                        ),
                                                        attr='minidom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='parseString',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='zf', ctx=Load()),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='content.xml', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='val', ctx=Store()),
                                            iter=List(
                                                elts=[
                                                    Constant(value='text:p', kind=None),
                                                    Constant(value='text:h', kind=None),
                                                    Constant(value='text:list', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='element', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='content', ctx=Load()),
                                                            attr='getElementsByTagName',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='val', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='buf', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Name(id='textToString', ctx=Load()),
                                                                    args=[Name(id='element', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value='\n', kind=None),
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
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='buf', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_index_pdf',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Index PDF documents', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='PDFResourceManager', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='buf', ctx=Store())],
                            value=Constant(value='', kind='u'),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='bin_data', ctx=Load()),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=b'%PDF-', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='f', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='bin_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='resource_manager', ctx=Store())],
                                            value=Call(
                                                func=Name(id='PDFResourceManager', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='io', ctx=Load()),
                                                            attr='StringIO',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='content', ctx=Store()),
                                                ),
                                                withitem(
                                                    context_expr=Call(
                                                        func=Name(id='TextConverter', ctx=Load()),
                                                        args=[
                                                            Name(id='resource_manager', ctx=Load()),
                                                            Name(id='content', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='device', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='logging', ctx=Load()),
                                                                    attr='getLogger',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='pdfminer', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='setLevel',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='logging', ctx=Load()),
                                                                attr='CRITICAL',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='interpreter', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='PDFPageInterpreter', ctx=Load()),
                                                        args=[
                                                            Name(id='resource_manager', ctx=Load()),
                                                            Name(id='device', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='page', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='PDFPage', ctx=Load()),
                                                            attr='get_pages',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='f', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='interpreter', ctx=Load()),
                                                                    attr='process_page',
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
                                                Assign(
                                                    targets=[Name(id='buf', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='content', ctx=Load()),
                                                            attr='getvalue',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='buf', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_index',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                            arg(arg='mimetype', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='ftype', ctx=Store()),
                            iter=Name(id='FTYPES', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='buf', ctx=Store())],
                                    value=Call(
                                        func=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='self', ctx=Load()),
                                                BinOp(
                                                    left=Constant(value='_index_%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='ftype', ctx=Load()),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[Name(id='bin_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='buf', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='buf', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='\x00', kind=None),
                                                    Constant(value='', kind=None),
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrAttachment', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_index',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bin_data', ctx=Load()),
                                    Name(id='mimetype', ctx=Load()),
                                ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
