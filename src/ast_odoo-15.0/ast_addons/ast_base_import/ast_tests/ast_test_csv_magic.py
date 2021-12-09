Module(
    body=[
        Expr(
            value=Constant(value='\nTests for various autodetection magics for CSV imports\n', kind=None),
        ),
        Import(
            names=[alias(name='codecs', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ImportCase',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_make_import',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='contents', annotation=None, type_comment=None),
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
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file_name', kind=None),
                                            Constant(value='file_type', kind=None),
                                            Constant(value='file', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.complex', kind=None),
                                            Constant(value='f', kind=None),
                                            Constant(value='text/csv', kind=None),
                                            Name(id='contents', ctx=Load()),
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
        ClassDef(
            name='TestEncoding',
            bases=[Name(id='ImportCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    create + parse_preview -> check result options\n    ', kind=None),
                ),
                FunctionDef(
                    name='_check_text',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                            arg(arg='encodings', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='options', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='quoting', kind=None),
                                    Constant(value='"', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='separator', kind=None),
                                    Constant(value='\t', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='test_text', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='text\tnumber\tdate\tdatetime\n%s\t1.23.45,67\t\t\n', kind=None),
                                op=Mod(),
                                right=Name(id='text', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='encoding', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='utf-8', kind=None),
                                    Constant(value='utf-16', kind=None),
                                    Constant(value='utf-32', kind=None),
                                    Starred(
                                        value=Name(id='encodings', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='encoding', ctx=Load()),
                                            Name(id='tuple', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='encoding', ctx=Store()),
                                                        Name(id='es', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='encoding', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='es', ctx=Store())],
                                            value=List(
                                                elts=[Name(id='encoding', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='preview', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_make_import',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='test_text', ctx=Load()),
                                                            attr='encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='encoding', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='parse_preview',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='options', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIsNone',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='preview', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='error', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='guessed', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='preview', ctx=Load()),
                                            slice=Constant(value='options', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='encoding', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIsNotNone',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='guessed', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='codecs', ctx=Load()),
                                                        attr='lookup',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='guessed', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ListComp(
                                                elt=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='codecs', ctx=Load()),
                                                            attr='lookup',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='e', ctx=Store()),
                                                        iter=Name(id='es', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_autodetect_encoding',
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
                            value=Constant(value=' Check that import preview can detect & return encoding\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Iñtërnâtiônàlizætiøn', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='iso-8859-1', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='iso-8859-1', kind=None),
                                                            Constant(value='iso-8859-2', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='やぶら小路の藪柑子。海砂利水魚の、食う寝る処に住む処、パイポパイポ パイポのシューリンガン。', kind=None),
                                    List(
                                        elts=[
                                            Constant(value='eucjp', kind=None),
                                            Constant(value='shift_jis', kind=None),
                                            Constant(value='iso2022_jp', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='대통령은 제4항과 제5항의 규정에 의하여 확정된 법률을 지체없이 공포하여야 한다, 탄핵의 결정.', kind=None),
                                    List(
                                        elts=[
                                            Constant(value='euc_kr', kind=None),
                                            Constant(value='iso2022_kr', kind=None),
                                        ],
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
                FunctionDef(
                    name='test_override_detection',
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
                            value=Constant(value=' ensure an explicitly specified encoding is not overridden by the\n        auto-detection\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='s', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='Iñtërnâtiônàlizætiøn', kind=None),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_make_import',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='s', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=b'\ntext', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='encoding', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value='\t', kind=None),
                                            Constant(value='iso-8859-1', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='r', ctx=Load()),
                                            slice=Constant(value='options', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='encoding', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='iso-8859-1', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='preview', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='s', ctx=Load()),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='iso-8859-1', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='text', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestFileSeparator',
            bases=[Name(id='ImportCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='imp',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_import',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='c|f\na|1\nb|2\nc|3\nd|4\n', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_explicit_success',
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
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='imp',
                                        ctx=Load(),
                                    ),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                            Constant(value='quoting', kind=None),
                                        ],
                                        values=[
                                            Constant(value='|', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='"', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='c', kind=None),
                                            Constant(value='f', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='preview', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='b', kind=None),
                                                    Constant(value='c', kind=None),
                                                    Constant(value='d', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='1', kind=None),
                                                    Constant(value='2', kind=None),
                                                    Constant(value='3', kind=None),
                                                    Constant(value='4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='r', ctx=Load()),
                                            slice=Constant(value='options', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='separator', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
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
                    name='test_explicit_fail',
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
                            value=Constant(value=" Don't protect user against making mistakes\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='imp',
                                        ctx=Load(),
                                    ),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                            Constant(value='quoting', kind=None),
                                        ],
                                        values=[
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='"', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='c|f', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='preview', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='a|1', kind=None),
                                                    Constant(value='b|2', kind=None),
                                                    Constant(value='c|3', kind=None),
                                                    Constant(value='d|4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='r', ctx=Load()),
                                            slice=Constant(value='options', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='separator', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=',', kind=None),
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
                    name='test_guess_ok',
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
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='imp',
                                        ctx=Load(),
                                    ),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                            Constant(value='quoting', kind=None),
                                        ],
                                        values=[
                                            Constant(value='', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='"', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='c', kind=None),
                                            Constant(value='f', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='preview', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='b', kind=None),
                                                    Constant(value='c', kind=None),
                                                    Constant(value='d', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='1', kind=None),
                                                    Constant(value='2', kind=None),
                                                    Constant(value='3', kind=None),
                                                    Constant(value='4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='r', ctx=Load()),
                                            slice=Constant(value='options', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='separator', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
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
                    name='test_noguess',
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
                            value=Constant(value=' If the guesser has no idea what the separator is, it defaults to\n        "," but should not set that value\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='imp', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_import',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='c\na\nb\nc\nd', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='imp', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                            Constant(value='quoting', kind=None),
                                        ],
                                        values=[
                                            Constant(value='', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='"', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='c', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='preview', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='b', kind=None),
                                                    Constant(value='c', kind=None),
                                                    Constant(value='d', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='r', ctx=Load()),
                                            slice=Constant(value='options', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='separator', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
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
        ClassDef(
            name='TestNumberSeparators',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_parse_float',
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
                            targets=[Name(id='w', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='res_model', kind=None)],
                                        values=[Constant(value='base_import.tests.models.float', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='w', ctx=Load()),
                                    attr='_parse_import_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='1.62', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='-1.62', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='+1.62', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='  +1.62  ', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='(1.62)', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value="1'234'567,89", kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value="1.234.567'89", kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='d', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='d', ctx=Store()),
                                                iter=Name(id='data', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='1.62', kind=None),
                                            Constant(value='-1.62', kind=None),
                                            Constant(value='+1.62', kind=None),
                                            Constant(value='+1.62', kind=None),
                                            Constant(value='-1.62', kind=None),
                                            Constant(value='1234567.89', kind=None),
                                            Constant(value='1234567.89', kind=None),
                                        ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
