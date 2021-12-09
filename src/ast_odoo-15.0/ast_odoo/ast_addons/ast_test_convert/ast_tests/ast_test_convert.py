Module(
    body=[
        Import(
            names=[alias(name='collections', asname=None)],
        ),
        Import(
            names=[alias(name='unittest', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname='ET')],
            level=0,
        ),
        ImportFrom(
            module='lxml.builder',
            names=[alias(name='E', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.convert',
            names=[
                alias(name='xml_import', asname=None),
                alias(name='_eval_xml', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='Field', ctx=Store())],
            value=Attribute(
                value=Name(id='E', ctx=Load()),
                attr='field',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='Value', ctx=Store())],
            value=Attribute(
                value=Name(id='E', ctx=Load()),
                attr='value',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='TestEvalXML',
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
                    name='eval_xml',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='node', annotation=None, type_comment=None),
                            arg(arg='obj', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='_eval_xml', ctx=Load()),
                                args=[
                                    Name(id='obj', ctx=Load()),
                                    Name(id='node', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
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
                    name='test_char',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='foo', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='foo', kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='None', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='None', kind=None),
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
                    name='test_int',
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
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='None', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='int', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='what the fuck?', kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value=' 42  ', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='int', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=42, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValueError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='4.82', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='int', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValueError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='Whelp', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='int', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                    name='test_float',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='4.78', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='float', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=4.78, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValueError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='None', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='float', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValueError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='Foo', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='float', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                    name='test_list',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='list', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='Value', ctx=Load()),
                                                        args=[Constant(value='foo', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='Value', ctx=Load()),
                                                        args=[Constant(value='5', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='type',
                                                                value=Constant(value='int', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Name(id='Value', ctx=Load()),
                                                        args=[Constant(value='4.76', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='type',
                                                                value=Constant(value='float', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Name(id='Value', ctx=Load()),
                                                        args=[Constant(value='None', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='type',
                                                                value=Constant(value='int', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='list', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='foo', kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=4.76, kind=None),
                                            Constant(value=None, kind=None),
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
                    name='test_file',
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
                            targets=[Name(id='Obj', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='collections', ctx=Load()),
                                    attr='namedtuple',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Obj', kind=None),
                                    List(
                                        elts=[
                                            Constant(value='module', kind=None),
                                            Constant(value='idref', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='obj', ctx=Store())],
                            value=Call(
                                func=Name(id='Obj', ctx=Load()),
                                args=[
                                    Constant(value='test_convert', kind=None),
                                    Constant(value=None, kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='test_file.txt', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='file', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Name(id='obj', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='test_convert,test_file.txt', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='IOError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eval_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='test_nofile.txt', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='file', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Name(id='obj', ctx=Load()),
                                        ],
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
                    name='test_function',
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
                            targets=[Name(id='obj', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_import', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Constant(value='test_convert', kind=None),
                                    Constant(value=None, kind=None),
                                    Constant(value='init', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='function',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='test_convert.usered', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='model_method', kind=None),
                                    ),
                                    keyword(
                                        arg='eval',
                                        value=Constant(value='[1, 2]', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='rec', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eval_xml',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xml', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
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
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    Name(id='args', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
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
                                    Name(id='kwargs', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='function',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='test_convert.usered', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='method', kind=None),
                                    ),
                                    keyword(
                                        arg='eval',
                                        value=Constant(value='[1, 2]', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='rec', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eval_xml',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xml', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
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
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value=1, kind=None)],
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
                                    Name(id='args', ctx=Load()),
                                    Tuple(
                                        elts=[Constant(value=2, kind=None)],
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
                                    Name(id='kwargs', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='function',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='1', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='2', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='test_convert.usered', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='model_method', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='rec', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eval_xml',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xml', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
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
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    Name(id='args', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
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
                                    Name(id='kwargs', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='function',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='1', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='2', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='test_convert.usered', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='method', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='rec', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eval_xml',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xml', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
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
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value=1, kind=None)],
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
                                    Name(id='args', ctx=Load()),
                                    Tuple(
                                        elts=[Constant(value=2, kind=None)],
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
                                    Name(id='kwargs', ctx=Load()),
                                    Dict(keys=[], values=[]),
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
                    name='test_function_kwargs',
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
                            targets=[Name(id='obj', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_import', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Constant(value='test_convert', kind=None),
                                    Constant(value=None, kind=None),
                                    Constant(value='init', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='function',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='1', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='foo', kind=None),
                                            ),
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='2', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='test_convert.usered', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='model_method', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='rec', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eval_xml',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xml', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
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
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    Name(id='args', ctx=Load()),
                                    Tuple(
                                        elts=[Constant(value=1, kind=None)],
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
                                    Name(id='kwargs', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='foo', kind=None)],
                                        values=[Constant(value=2, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='function',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='1', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='foo', kind=None),
                                            ),
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='2', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='test_convert.usered', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='method', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='rec', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eval_xml',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xml', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
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
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value=1, kind=None)],
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
                                    Name(id='args', ctx=Load()),
                                    Tuple(elts=[], ctx=Load()),
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
                                    Name(id='kwargs', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='foo', kind=None)],
                                        values=[Constant(value=2, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='function',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='1', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='context', kind=None),
                                            ),
                                            keyword(
                                                arg='eval',
                                                value=Constant(value="{'foo': 2}", kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='test_convert.usered', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='model_method', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='rec', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eval_xml',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xml', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='foo', kind=None)],
                                        values=[Constant(value=2, kind=None)],
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
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    Name(id='args', ctx=Load()),
                                    Tuple(
                                        elts=[Constant(value=1, kind=None)],
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
                                    Name(id='kwargs', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='function',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='1', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='context', kind=None),
                                            ),
                                            keyword(
                                                arg='eval',
                                                value=Constant(value="{'foo': 2}", kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='test_convert.usered', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='method', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='rec', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eval_xml',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xml', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='foo', kind=None)],
                                        values=[Constant(value=2, kind=None)],
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
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value=1, kind=None)],
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
                                    Name(id='args', ctx=Load()),
                                    Tuple(elts=[], ctx=Load()),
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
                                    Name(id='kwargs', ctx=Load()),
                                    Dict(keys=[], values=[]),
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
                    name='test_function_function',
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
                            targets=[Name(id='obj', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_import', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Constant(value='test_convert', kind=None),
                                    Constant(value=None, kind=None),
                                    Constant(value='init', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='function',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='function',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='model',
                                                value=Constant(value='test_convert.usered', kind=None),
                                            ),
                                            keyword(
                                                arg='name',
                                                value=Constant(value='search', kind=None),
                                            ),
                                            keyword(
                                                arg='eval',
                                                value=Constant(value='[[]]', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='test_convert.usered', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='method', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='rec', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eval_xml',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xml', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
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
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    Name(id='args', ctx=Load()),
                                    Tuple(elts=[], ctx=Load()),
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
                                    Name(id='kwargs', ctx=Load()),
                                    Dict(keys=[], values=[]),
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
                    name='test_xml',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='unittest', ctx=Load()),
                                attr='skip',
                                ctx=Load(),
                            ),
                            args=[Constant(value='not tested', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='unittest', ctx=Load()),
                                attr='skip',
                                ctx=Load(),
                            ),
                            args=[Constant(value='not tested', kind=None)],
                            keywords=[],
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
