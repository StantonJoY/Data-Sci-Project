Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
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
                    module='OpenSSL',
                    names=[alias(name='crypto', asname='ssl_crypto')],
                    level=0,
                ),
                Import(
                    names=[alias(name='OpenSSL._util', asname='ssl_util')],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='ssl_crypto', ctx=Store())],
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
                                args=[Constant(value="Cannot import library 'OpenSSL' for PKCS#7 envelope extraction.", kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        FunctionDef(
            name='remove_signature',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Remove the PKCS#7 envelope from given content, making a '.xml.p7m' file content readable as it was '.xml'.\n        As OpenSSL may not be installed, in that case a warning is issued and None is returned. ", kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='ssl_crypto', ctx=Load()),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Error reading the content, check if the OpenSSL library is installed for for PKCS#7 envelope extraction.', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='null', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='ssl_util', ctx=Load()),
                            attr='ffi',
                            ctx=Load(),
                        ),
                        attr='NULL',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='verify', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='ssl_util', ctx=Load()),
                            attr='lib',
                            ctx=Load(),
                        ),
                        attr='PKCS7_verify',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='flags', ctx=Store())],
                    value=BinOp(
                        left=Attribute(
                            value=Attribute(
                                value=Name(id='ssl_util', ctx=Load()),
                                attr='lib',
                                ctx=Load(),
                            ),
                            attr='PKCS7_NOVERIFY',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Attribute(
                                value=Name(id='ssl_util', ctx=Load()),
                                attr='lib',
                                ctx=Load(),
                            ),
                            attr='PKCS7_NOSIGS',
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='out_buffer', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='ssl_crypto', ctx=Load()),
                            attr='_new_mem_buf',
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
                                func=Attribute(
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='catch_warnings',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=None,
                        ),
                    ],
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='filterwarnings',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ignore', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='category',
                                        value=Name(id='DeprecationWarning', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='loaded_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ssl_crypto', ctx=Load()),
                                    attr='load_pkcs7_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='ssl_crypto', ctx=Load()),
                                        attr='FILETYPE_ASN1',
                                        ctx=Load(),
                                    ),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='verify', ctx=Load()),
                            args=[
                                Attribute(
                                    value=Name(id='loaded_data', ctx=Load()),
                                    attr='_pkcs7',
                                    ctx=Load(),
                                ),
                                Name(id='null', ctx=Load()),
                                Name(id='null', ctx=Load()),
                                Name(id='null', ctx=Load()),
                                Name(id='out_buffer', ctx=Load()),
                                Name(id='flags', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                        ops=[NotEq()],
                        comparators=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ssl_crypto', ctx=Load()),
                                    attr='_raise_current_error',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='decoded_content', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='ssl_crypto', ctx=Load()),
                            attr='_bio_to_string',
                            ctx=Load(),
                        ),
                        args=[Name(id='out_buffer', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='decoded_content', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
