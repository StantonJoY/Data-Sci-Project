Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='pathlib',
            names=[alias(name='Path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules',
            names=[
                alias(name='get_modules', asname=None),
                alias(name='get_module_path', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='lint_case', asname=None)],
            level=1,
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
            targets=[Name(id='WHITELIST', ctx=Store())],
            value=List(
                elts=[Constant(value='test_data_module', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='TestDunderinit',
            bases=[
                Attribute(
                    value=Name(id='lint_case', ctx=Load()),
                    attr='LintCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_dunderinit',
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
                            value=Constant(value=" Test that __init__.py exists in Odoo modules, otherwise they won't get packaged", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='modules_list', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='mod', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='mod', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='get_modules', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                left=Name(id='mod', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='WHITELIST', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='mod', ctx=Store()),
                            iter=Name(id='modules_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='dunderinit_path', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='Path', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='get_module_path', ctx=Load()),
                                                    args=[Name(id='mod', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Div(),
                                        right=Constant(value='__init__.py', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='dunderinit_path', ctx=Load()),
                                                    attr='is_file',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                left=Constant(value='Missing `__init__.py ` in module %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='mod', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%s modules checked', kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='modules_list', ctx=Load())],
                                        keywords=[],
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
