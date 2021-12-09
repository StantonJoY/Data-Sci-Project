Module(
    body=[
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='cloc', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='XML_TEST', ctx=Store())],
            value=Constant(value='<!-- Comment -->\n<?xml version="1.0" encoding="UTF-8"?>\n<odoo>\n    <node>Line</node>\n    <!-- Comment -->\n    <node>Line</node>\n    <!-- Comment\n        Multi\n    Line -->\n    <![CDATA[\n        Line\n    ]]>\n    <![CDATA[\n        <!-- comment in CDATA -->\n        cdata Line\n    yes6]]>\n    <![CDATA[<!-- not a comment-->]]>\n    <![CDATA[<!-- not a comment\n     but counted as is\n    -->]]>\n    <!-- <![CDATA[ This is a valid comment ]]> -->\n    <!-- <![CDATA[ Multi line\n    comment]]> -->\n    <record id="my_id" model="model">\n        <field name="name">name</field>\n    </record>\n    <![CDATA[ <!-- no a comment]]>\n    <node>not a comment but found as is</node>\n    <!-- comment -->\n    <node>After closed comment back to normal</node>\n</odoo>\n', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='PY_TEST_NO_RETURN', ctx=Store())],
            value=Constant(value='line = 1\nline = 2', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='PY_TEST', ctx=Store())],
            value=Constant(value='\n# comment 1\n\ndef func(): # eol comment 3\n    """ docstring\n    """\n    pass\n\ndef query():\n    long_query = """\n        SELECT *\n        FROM table\n        WHERE id = 1;\n    """\n    return query\n\nprint(i.lineno, i, getattr(i,\'s\',None), getattr(i,\'value\',None))\n', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='JS_TEST', ctx=Store())],
            value=Constant(value='\n/*\ncomment\n*/\n\nfunction() {\n    return 1+2; // comment\n}\n\nfunction() {\n    hello = 4; /*\n        comment\n    */\n    console.log(hello);\n    regex = /\\/*h/;\n    legit_code_counted = 1;\n    regex2 = /.*/;\n}\n', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='TestCloc',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_parser',
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
                            targets=[Name(id='cl', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cloc', ctx=Load()),
                                    attr='Cloc',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cl', ctx=Load()),
                                    attr='parse_xml',
                                    ctx=Load(),
                                ),
                                args=[Name(id='XML_TEST', ctx=Load())],
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
                                    Name(id='xml_count', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Constant(value=18, kind=None),
                                            Constant(value=31, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='py_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cl', ctx=Load()),
                                    attr='parse_py',
                                    ctx=Load(),
                                ),
                                args=[Name(id='PY_TEST_NO_RETURN', ctx=Load())],
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
                                    Name(id='py_count', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Constant(value=2, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='py_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cl', ctx=Load()),
                                    attr='parse_py',
                                    ctx=Load(),
                                ),
                                args=[Name(id='PY_TEST', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='version_info',
                                    ctx=Load(),
                                ),
                                ops=[GtE()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
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
                                            Name(id='py_count', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Constant(value=7, kind=None),
                                                    Constant(value=16, kind=None),
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='py_count', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Constant(value=8, kind=None),
                                                    Constant(value=16, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='js_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cl', ctx=Load()),
                                    attr='parse_js',
                                    ctx=Load(),
                                ),
                                args=[Name(id='JS_TEST', ctx=Load())],
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
                                    Name(id='js_count', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Constant(value=10, kind=None),
                                            Constant(value=17, kind=None),
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
