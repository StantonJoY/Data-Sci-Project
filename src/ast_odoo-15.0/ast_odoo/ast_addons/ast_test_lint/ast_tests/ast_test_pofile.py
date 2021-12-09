Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='Counter', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules',
            names=[
                alias(name='get_modules', asname=None),
                alias(name='get_resource_path', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='TranslationFileReader', asname=None)],
            level=0,
        ),
        ClassDef(
            name='PotLinter',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_pot_duplicate_entries',
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
                        FunctionDef(
                            name='format',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='entry', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='entry', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='model', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Constant(value='model', kind=None),
                                                    Subscript(
                                                        value=Name(id='entry', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='entry', ctx=Load()),
                                                        slice=Constant(value='imd_name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='entry', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='model_terms', kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=Tuple(
                                                        elts=[
                                                            Constant(value='model_terms', kind=None),
                                                            Subscript(
                                                                value=Name(id='entry', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='entry', ctx=Load()),
                                                                slice=Constant(value='imd_name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='entry', ctx=Load()),
                                                                slice=Constant(value='src', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='entry', ctx=Load()),
                                                            slice=Constant(value='type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='code', kind=None)],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Tuple(
                                                                elts=[
                                                                    Constant(value='code', kind=None),
                                                                    Subscript(
                                                                        value=Name(id='entry', ctx=Load()),
                                                                        slice=Constant(value='src', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='module', ctx=Store()),
                            iter=Call(
                                func=Name(id='get_modules', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filename', ctx=Store())],
                                    value=Call(
                                        func=Name(id='get_resource_path', ctx=Load()),
                                        args=[
                                            Name(id='module', ctx=Load()),
                                            Constant(value='i18n', kind=None),
                                            BinOp(
                                                left=Name(id='module', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value='.pot', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='filename', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='counts', ctx=Store())],
                                    value=Call(
                                        func=Name(id='Counter', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='map', ctx=Load()),
                                                args=[
                                                    Name(id='format', ctx=Load()),
                                                    Call(
                                                        func=Name(id='TranslationFileReader', ctx=Load()),
                                                        args=[Name(id='filename', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='duplicates', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='key', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='key', ctx=Store()),
                                                        Name(id='count', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='counts', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='count', ctx=Load()),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=1, kind=None)],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertFalse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='duplicates', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Duplicate entries found in %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='filename', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
