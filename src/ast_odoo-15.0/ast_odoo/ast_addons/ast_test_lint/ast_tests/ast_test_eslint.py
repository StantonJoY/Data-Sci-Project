Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        ImportFrom(
            module='unittest',
            names=[alias(name='skipIf', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='lint_case', asname=None)],
            level=1,
        ),
        Assign(
            targets=[Name(id='RULES', ctx=Store())],
            value=Constant(value='{"no-undef": "error","no-restricted-globals": ["error", "event", "self"],"no-const-assign": ["error"],"no-debugger": ["error"],"no-dupe-class-members": ["error"]}', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='PARSER_OPTIONS', ctx=Store())],
            value=Constant(value='{ecmaVersion: 2019, sourceType: module}', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GLOBAL', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Constant(value=',', kind=None),
                    attr='join',
                    ctx=Load(),
                ),
                args=[
                    List(
                        elts=[
                            Constant(value='owl', kind=None),
                            Constant(value='odoo', kind=None),
                            Constant(value='$', kind=None),
                            Constant(value='jQuery', kind=None),
                            Constant(value='_', kind=None),
                            Constant(value='Chart', kind=None),
                            Constant(value='fuzzy', kind=None),
                            Constant(value='QWeb2', kind=None),
                            Constant(value='Popover', kind=None),
                            Constant(value='StackTrace', kind=None),
                            Constant(value='QUnit', kind=None),
                            Constant(value='luxon', kind=None),
                            Constant(value='moment', kind=None),
                            Constant(value='py', kind=None),
                            Constant(value='ClipboardJS', kind=None),
                            Constant(value='globalThis', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
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
        Try(
            body=[
                Assign(
                    targets=[Name(id='eslint', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='misc',
                                ctx=Load(),
                            ),
                            attr='find_in_path',
                            ctx=Load(),
                        ),
                        args=[Constant(value='eslint', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='IOError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='eslint', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        ClassDef(
            name='TestESLint',
            bases=[
                Attribute(
                    value=Name(id='lint_case', ctx=Load()),
                    attr='LintCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='longMessage', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_eslint_version',
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
                            value=Constant(value=' Test that there are no eslint errors in javascript files ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='files_to_check', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='p', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='p', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='iter_module_files',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='**/static/**/*.js', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='match',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='.*/libs?/.*', kind=None),
                                                        Name(id='p', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Testing %s js files', kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='files_to_check', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cmd', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Name(id='eslint', ctx=Load()),
                                        Constant(value='--no-eslintrc', kind=None),
                                        Constant(value='--env', kind=None),
                                        Constant(value='browser', kind=None),
                                        Constant(value='--env', kind=None),
                                        Constant(value='es2017', kind=None),
                                        Constant(value='--parser-options', kind=None),
                                        Name(id='PARSER_OPTIONS', ctx=Load()),
                                        Constant(value='--rule', kind=None),
                                        Name(id='RULES', ctx=Load()),
                                        Constant(value='--global', kind=None),
                                        Name(id='GLOBAL', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Name(id='files_to_check', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='process', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[Name(id='cmd', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='stdout',
                                        value=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='PIPE',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='stderr',
                                        value=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='DEVNULL',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='check',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                        value=Name(id='process', ctx=Load()),
                                        attr='returncode',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='process', ctx=Load()),
                                                    attr='stdout',
                                                    ctx=Load(),
                                                ),
                                                attr='decode',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='skipIf', ctx=Load()),
                    args=[
                        Compare(
                            left=Name(id='eslint', ctx=Load()),
                            ops=[Is()],
                            comparators=[Constant(value=None, kind=None)],
                        ),
                        Constant(value='eslint tool not found on this system', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
