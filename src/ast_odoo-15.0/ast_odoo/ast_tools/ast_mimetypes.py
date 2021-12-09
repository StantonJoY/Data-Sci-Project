Module(
    body=[
        Expr(
            value=Constant(value='\nMimetypes-related utilities\n\n# TODO: reexport stdlib mimetypes?\n', kind=None),
        ),
        Import(
            names=[alias(name='collections', asname=None)],
        ),
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='zipfile', asname=None)],
        ),
        Assign(
            targets=[Name(id='__all__', ctx=Store())],
            value=List(
                elts=[Constant(value='guess_mimetype', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
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
            targets=[Name(id='_ooxml_dirs', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='word/', kind=None),
                    Constant(value='pt/', kind=None),
                    Constant(value='xl/', kind=None),
                ],
                values=[
                    Constant(value='application/vnd.openxmlformats-officedocument.wordprocessingml.document', kind=None),
                    Constant(value='application/vnd.openxmlformats-officedocument.presentationml.presentation', kind=None),
                    Constant(value='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_check_ooxml',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='data', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            optional_vars=Name(id='f', ctx=Store()),
                        ),
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='zipfile', ctx=Load()),
                                    attr='ZipFile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='f', ctx=Load())],
                                keywords=[],
                            ),
                            optional_vars=Name(id='z', ctx=Store()),
                        ),
                    ],
                    body=[
                        Assign(
                            targets=[Name(id='filenames', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='z', ctx=Load()),
                                    attr='namelist',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='[Content_Types].xml', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='filenames', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='dirname', ctx=Store()),
                                    Name(id='mime', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='_ooxml_dirs', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='entry', ctx=Load()),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='dirname', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='entry', ctx=Store()),
                                                        iter=Name(id='filenames', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='mime', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
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
            targets=[Name(id='_mime_validator', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    [\\w-]+ # type-name\n    / # subtype separator\n    [\\w-]+ # registration facet or subtype\n    (?:\\.[\\w-]+)* # optional faceted name\n    (?:\\+[\\w-]+)? # optional structured syntax specifier\n', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='VERBOSE',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_check_open_container_format',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='data', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            optional_vars=Name(id='f', ctx=Store()),
                        ),
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='zipfile', ctx=Load()),
                                    attr='ZipFile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='f', ctx=Load())],
                                keywords=[],
                            ),
                            optional_vars=Name(id='z', ctx=Store()),
                        ),
                    ],
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='mimetype', kind=None),
                                ops=[NotIn()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='z', ctx=Load()),
                                            attr='namelist',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='marcel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='z', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mimetype', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ascii', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='marcel', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=256, kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='_mime_validator', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='marcel', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='marcel', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
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
            targets=[Name(id='_xls_pattern', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value=b'\n    \t\x08\x10\x00\x00\x06\x05\x00\n  | \xfd\xff\xff\xff(\x10|\x1f| |"|\\#|\\(|\\))\n', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='VERBOSE',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_ppt_pattern', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value=b'\n    \x00n\x1e\xf0\n  | \x0f\x00\xe8\x03\n  | \xa0F\x1d\xf0\n  | \xfd\xff\xff\xff(\x0e|\x1c|C)\x00\x00\x00\n', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='VERBOSE',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_check_olecf',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='data', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Pre-OOXML Office formats are OLE Compound Files which all use the same\n    file signature ("magic bytes") and should have a subheader at offset 512\n    (0x200).\n\n    Subheaders taken from http://www.garykessler.net/library/file_sigs.html\n    according to which Mac office files *may* have different subheaders. We\'ll\n    ignore that.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='offset', ctx=Store())],
                    value=Constant(value=512, kind=None),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='data', ctx=Load()),
                            attr='startswith',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value=b'\xec\xa5\xc1\x00', kind=None),
                            Name(id='offset', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value='application/msword', kind=None),
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Constant(value=b'Microsoft Excel', kind=None),
                                ops=[In()],
                                comparators=[Name(id='data', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='application/vnd.ms-excel', kind=None),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='_ppt_pattern', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='data', ctx=Load()),
                                            Name(id='offset', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value='application/vnd.ms-powerpoint', kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
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
            name='_check_svg',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='data', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='This simply checks the existence of the opening and ending SVG tags', kind=None),
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Constant(value=b'<svg', kind=None),
                                ops=[In()],
                                comparators=[Name(id='data', ctx=Load())],
                            ),
                            Compare(
                                left=Constant(value=b'/svg>', kind=None),
                                ops=[In()],
                                comparators=[Name(id='data', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value='image/svg+xml', kind=None),
                        ),
                    ],
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_Entry', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='collections', ctx=Load()),
                    attr='namedtuple',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='_Entry', kind=None),
                    List(
                        elts=[
                            Constant(value='mimetype', kind=None),
                            Constant(value='signatures', kind=None),
                            Constant(value='discriminants', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_mime_mappings', ctx=Store())],
            value=Tuple(
                elts=[
                    Call(
                        func=Name(id='_Entry', ctx=Load()),
                        args=[
                            Constant(value='application/pdf', kind=None),
                            List(
                                elts=[Constant(value=b'%PDF', kind=None)],
                                ctx=Load(),
                            ),
                            List(elts=[], ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='_Entry', ctx=Load()),
                        args=[
                            Constant(value='image/jpeg', kind=None),
                            List(
                                elts=[
                                    Constant(value=b'\xff\xd8\xff\xe0', kind=None),
                                    Constant(value=b'\xff\xd8\xff\xe2', kind=None),
                                    Constant(value=b'\xff\xd8\xff\xe3', kind=None),
                                    Constant(value=b'\xff\xd8\xff\xe1', kind=None),
                                    Constant(value=b'\xff\xd8\xff\xdb', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            List(elts=[], ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='_Entry', ctx=Load()),
                        args=[
                            Constant(value='image/png', kind=None),
                            List(
                                elts=[Constant(value=b'\x89PNG\r\n\x1a\n', kind=None)],
                                ctx=Load(),
                            ),
                            List(elts=[], ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='_Entry', ctx=Load()),
                        args=[
                            Constant(value='image/gif', kind=None),
                            List(
                                elts=[
                                    Constant(value=b'GIF87a', kind=None),
                                    Constant(value=b'GIF89a', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            List(elts=[], ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='_Entry', ctx=Load()),
                        args=[
                            Constant(value='image/bmp', kind=None),
                            List(
                                elts=[Constant(value=b'BM', kind=None)],
                                ctx=Load(),
                            ),
                            List(elts=[], ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='_Entry', ctx=Load()),
                        args=[
                            Constant(value='image/svg+xml', kind=None),
                            List(
                                elts=[Constant(value=b'<', kind=None)],
                                ctx=Load(),
                            ),
                            List(
                                elts=[Name(id='_check_svg', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='_Entry', ctx=Load()),
                        args=[
                            Constant(value='image/x-icon', kind=None),
                            List(
                                elts=[Constant(value=b'\x00\x00\x01\x00', kind=None)],
                                ctx=Load(),
                            ),
                            List(elts=[], ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='_Entry', ctx=Load()),
                        args=[
                            Constant(value='application/msword', kind=None),
                            List(
                                elts=[
                                    Constant(value=b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1', kind=None),
                                    Constant(value=b'\rDOC', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            List(
                                elts=[Name(id='_check_olecf', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='_Entry', ctx=Load()),
                        args=[
                            Constant(value='application/zip', kind=None),
                            List(
                                elts=[Constant(value=b'PK\x03\x04', kind=None)],
                                ctx=Load(),
                            ),
                            List(
                                elts=[
                                    Name(id='_check_ooxml', ctx=Load()),
                                    Name(id='_check_open_container_format', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_odoo_guess_mimetype',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='bin_data', annotation=None, type_comment=None),
                    arg(arg='default', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='application/octet-stream', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Attempts to guess the mime type of the provided binary data, similar\n    to but significantly more limited than libmagic\n\n    :param str bin_data: binary data to try and guess a mime type for\n    :returns: matched mimetype or ``application/octet-stream`` if none matched\n    ', kind=None),
                ),
                For(
                    target=Name(id='entry', ctx=Store()),
                    iter=Name(id='_mime_mappings', ctx=Load()),
                    body=[
                        For(
                            target=Name(id='signature', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='entry', ctx=Load()),
                                attr='signatures',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='bin_data', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='signature', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='discriminant', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='entry', ctx=Load()),
                                                attr='discriminants',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='guess', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='discriminant', ctx=Load()),
                                                                args=[Name(id='bin_data', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='guess', ctx=Load()),
                                                            body=[
                                                                Return(
                                                                    value=Name(id='guess', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='Exception', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='_logger', ctx=Load()),
                                                                                    attr='getChild',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='guess_mimetype', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='warn',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value="Sub-checker '%s' of type '%s' failed", kind=None),
                                                                            Attribute(
                                                                                value=Name(id='discriminant', ctx=Load()),
                                                                                attr='__name__',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='entry', ctx=Load()),
                                                                                attr='mimetype',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='exc_info',
                                                                                value=Constant(value=True, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Attribute(
                                                value=Name(id='entry', ctx=Load()),
                                                attr='mimetype',
                                                ctx=Load(),
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
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='default', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='magic', asname=None)],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='magic', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        If(
            test=Name(id='magic', ctx=Load()),
            body=[
                If(
                    test=Call(
                        func=Name(id='hasattr', ctx=Load()),
                        args=[
                            Name(id='magic', ctx=Load()),
                            Constant(value='from_buffer', kind=None),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='_guesser', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='functools', ctx=Load()),
                                    attr='partial',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='magic', ctx=Load()),
                                        attr='from_buffer',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='mime',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='magic', ctx=Load()),
                                    Constant(value='open', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ms', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='magic', ctx=Load()),
                                            attr='open',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='magic', ctx=Load()),
                                                attr='MAGIC_MIME_TYPE',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ms', ctx=Load()),
                                            attr='load',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='_guesser', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='ms', ctx=Load()),
                                        attr='buffer',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
                FunctionDef(
                    name='guess_mimetype',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='bin_data', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='_guesser', ctx=Load()),
                                args=[Name(id='bin_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='mimetype', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='image/svg', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='image/svg+xml', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='mimetype', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            orelse=[
                Assign(
                    targets=[Name(id='guess_mimetype', ctx=Store())],
                    value=Name(id='_odoo_guess_mimetype', ctx=Load()),
                    type_comment=None,
                ),
            ],
        ),
        FunctionDef(
            name='neuter_mimetype',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='mimetype', annotation=None, type_comment=None),
                    arg(arg='user', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='wrong_type', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Constant(value='ht', kind=None),
                                ops=[In()],
                                comparators=[Name(id='mimetype', ctx=Load())],
                            ),
                            Compare(
                                left=Constant(value='xml', kind=None),
                                ops=[In()],
                                comparators=[Name(id='mimetype', ctx=Load())],
                            ),
                            Compare(
                                left=Constant(value='svg', kind=None),
                                ops=[In()],
                                comparators=[Name(id='mimetype', ctx=Load())],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='wrong_type', ctx=Load()),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='_is_system',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value='text/plain', kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='mimetype', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
