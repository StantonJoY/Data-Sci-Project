Module(
    body=[
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='platform', asname=None)],
        ),
        Import(
            names=[alias(name='psutil', asname=None)],
        ),
        Import(
            names=[alias(name='unittest', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[alias(name='TransactionCaseWithUserDemo', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='CacheMiss', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestRecordCache',
            bases=[Name(id='TransactionCaseWithUserDemo', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_cache',
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
                            value=Constant(value=' Check the record cache object. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id='type', ctx=Load()),
                                    args=[Name(id='Model', ctx=Load())],
                                    keywords=[],
                                ),
                                attr='name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id='type', ctx=Load()),
                                    args=[Name(id='Model', ctx=Load())],
                                    keywords=[],
                                ),
                                attr='ref',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cache', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='cache',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='check1',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='record', annotation=None, type_comment=None),
                                    arg(arg='field', annotation=None, type_comment=None),
                                    arg(arg='value', annotation=None, type_comment=None),
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='cache', ctx=Load()),
                                                    attr='contains',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='record', ctx=Load()),
                                                    Name(id='field', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Try(
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
                                                            value=Name(id='cache', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='record', ctx=Load()),
                                                            Name(id='field', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Name(id='value', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIsNotNone',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='CacheMiss', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertIsNone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Compare(
                                                left=Name(id='field', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cache', ctx=Load()),
                                                            attr='get_fields',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='record', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
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
                                            Compare(
                                                left=Name(id='record', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cache', ctx=Load()),
                                                            attr='get_records',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='record', ctx=Load()),
                                                            Name(id='field', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
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
                            name='check',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='record', annotation=None, type_comment=None),
                                    arg(arg='name_val', annotation=None, type_comment=None),
                                    arg(arg='ref_val', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=" check the values of fields 'name' and 'ref' on record. ", kind=None),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='check1', ctx=Load()),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                            Name(id='name_val', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='check1', ctx=Load()),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='ref', ctx=Load()),
                                            Name(id='ref_val', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='foo1', ctx=Store()),
                                        Name(id='bar1', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Model', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='foo2', ctx=Store()),
                                        Name(id='bar2', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Model', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_demo',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='foo1', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='foo2', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cache', ctx=Load()),
                                    attr='invalidate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo1', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo2', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar1', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar2', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cache', ctx=Load()),
                                            attr='get_missing_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='foo1', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='bar1', ctx=Load()),
                                            ),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
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
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cache', ctx=Load()),
                                            attr='get_missing_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='foo2', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='bar2', ctx=Load()),
                                            ),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
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
                                    value=Name(id='cache', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='foo1', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Constant(value='FOO1_NAME', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cache', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='foo1', ctx=Load()),
                                    Name(id='ref', ctx=Load()),
                                    Constant(value='FOO1_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cache', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bar1', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Constant(value='BAR1_NAME', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cache', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bar1', ctx=Load()),
                                    Name(id='ref', ctx=Load()),
                                    Constant(value='BAR1_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo1', ctx=Load()),
                                    Constant(value='FOO1_NAME', kind=None),
                                    Constant(value='FOO1_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo2', ctx=Load()),
                                    Constant(value='FOO1_NAME', kind=None),
                                    Constant(value='FOO1_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar1', ctx=Load()),
                                    Constant(value='BAR1_NAME', kind=None),
                                    Constant(value='BAR1_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar2', ctx=Load()),
                                    Constant(value='BAR1_NAME', kind=None),
                                    Constant(value='BAR1_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cache', ctx=Load()),
                                            attr='get_missing_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='foo1', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='bar1', ctx=Load()),
                                            ),
                                            Name(id='name', ctx=Load()),
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
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cache', ctx=Load()),
                                            attr='get_missing_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='foo2', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='bar2', ctx=Load()),
                                            ),
                                            Name(id='name', ctx=Load()),
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
                                    value=Name(id='cache', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='foo2', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Constant(value='FOO2_NAME', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cache', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='foo2', ctx=Load()),
                                    Name(id='ref', ctx=Load()),
                                    Constant(value='FOO2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cache', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bar2', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Constant(value='BAR2_NAME', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cache', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bar2', ctx=Load()),
                                    Name(id='ref', ctx=Load()),
                                    Constant(value='BAR2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo1', ctx=Load()),
                                    Constant(value='FOO2_NAME', kind=None),
                                    Constant(value='FOO2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo2', ctx=Load()),
                                    Constant(value='FOO2_NAME', kind=None),
                                    Constant(value='FOO2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar1', ctx=Load()),
                                    Constant(value='BAR2_NAME', kind=None),
                                    Constant(value='BAR2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar2', ctx=Load()),
                                    Constant(value='BAR2_NAME', kind=None),
                                    Constant(value='BAR2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cache', ctx=Load()),
                                            attr='get_missing_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='foo1', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='bar1', ctx=Load()),
                                            ),
                                            Name(id='name', ctx=Load()),
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
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cache', ctx=Load()),
                                            attr='get_missing_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='foo2', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='bar2', ctx=Load()),
                                            ),
                                            Name(id='name', ctx=Load()),
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
                                    value=Name(id='cache', ctx=Load()),
                                    attr='remove',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='foo1', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo1', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value='FOO2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo2', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value='FOO2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar1', ctx=Load()),
                                    Constant(value='BAR2_NAME', kind=None),
                                    Constant(value='BAR2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar2', ctx=Load()),
                                    Constant(value='BAR2_NAME', kind=None),
                                    Constant(value='BAR2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cache', ctx=Load()),
                                            attr='get_missing_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='foo1', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='bar1', ctx=Load()),
                                            ),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        keywords=[],
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
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cache', ctx=Load()),
                                            attr='get_missing_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='foo2', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='bar2', ctx=Load()),
                                            ),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        keywords=[],
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
                                    value=Name(id='cache', ctx=Load()),
                                    attr='invalidate',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Name(id='name', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='ref', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='foo1', ctx=Load()),
                                                        attr='ids',
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo1', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo2', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar1', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value='BAR2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar2', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value='BAR2_REF', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cache', ctx=Load()),
                                    attr='invalidate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo1', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='foo2', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar1', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Name(id='bar2', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
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
                    name='test_memory',
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
                            value=Constant(value=' Check memory consumption of the cache. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='NB_RECORDS', ctx=Store())],
                            value=Constant(value=100000, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='MAX_MEMORY', ctx=Store())],
                            value=Constant(value=100, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cache', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='cache',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='new',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='index', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[Name(id='NB_RECORDS', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='process', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='psutil', ctx=Load()),
                                    attr='Process',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='getpid',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rss0', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='process', ctx=Load()),
                                        attr='memory_info',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='rss',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='char_names', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='name', kind=None),
                                    Constant(value='display_name', kind=None),
                                    Constant(value='email', kind=None),
                                    Constant(value='website', kind=None),
                                    Constant(value='phone', kind=None),
                                    Constant(value='mobile', kind=None),
                                    Constant(value='street', kind=None),
                                    Constant(value='street2', kind=None),
                                    Constant(value='city', kind=None),
                                    Constant(value='zip', kind=None),
                                    Constant(value='vat', kind=None),
                                    Constant(value='ref', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='name', ctx=Store()),
                            iter=Name(id='char_names', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='field', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='_fields',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cache', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='record', ctx=Load()),
                                                    Name(id='field', ctx=Load()),
                                                    Constant(value='test', kind=None),
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
                        Assign(
                            targets=[Name(id='mem_usage', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='process', ctx=Load()),
                                            attr='memory_info',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='rss',
                                    ctx=Load(),
                                ),
                                op=Sub(),
                                right=Name(id='rss0', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mem_usage', ctx=Load()),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='MAX_MEMORY', ctx=Load()),
                                            op=Mult(),
                                            right=Constant(value=1024, kind=None),
                                        ),
                                        op=Mult(),
                                        right=Constant(value=1024, kind=None),
                                    ),
                                    BinOp(
                                        left=Constant(value='Caching %s records must take less than %sMB of memory', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='NB_RECORDS', ctx=Load()),
                                                Name(id='MAX_MEMORY', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='unittest', ctx=Load()),
                                attr='skipIf',
                                ctx=Load(),
                            ),
                            args=[
                                UnaryOp(
                                    op=Not(),
                                    operand=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='platform', ctx=Load()),
                                                        attr='system',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='Linux', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='platform', ctx=Load()),
                                                        attr='machine',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='x86_64', kind=None)],
                                            ),
                                        ],
                                    ),
                                ),
                                Constant(value='This test only makes sense on 64-bit Linux-like systems', kind=None),
                            ],
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
