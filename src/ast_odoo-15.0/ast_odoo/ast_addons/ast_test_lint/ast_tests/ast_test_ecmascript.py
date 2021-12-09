Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
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
            targets=[Name(id='MAX_ES_VERSION', ctx=Store())],
            value=Constant(value='es10', kind=None),
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
                    targets=[Name(id='es_check', ctx=Store())],
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
                        args=[Constant(value='es-check', kind=None)],
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
                            targets=[Name(id='es_check', ctx=Store())],
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
            name='TestECMAScriptVersion',
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
                    name='test_ecmascript_version',
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
                            value=Constant(value=' Test that there is no unsupported ecmascript in javascript files ', kind=None),
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
                                            args=[Constant(value='*.js', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                left=Constant(value='static/test', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='p', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='static/src/tests', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='p', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='static/lib/qweb/qweb.js', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='p', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='py.js/lib/py.js', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='p', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='static/lib/epos-2.12.0.js', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='p', ctx=Load())],
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
                                        Name(id='es_check', ctx=Load()),
                                        Name(id='MAX_ES_VERSION', ctx=Load()),
                                        Constant(value='--module', kind=None),
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
                                    attr='Popen',
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
                                            attr='PIPE',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='out', ctx=Store()),
                                        Name(id='err', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='process', ctx=Load()),
                                    attr='communicate',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                                value=Name(id='out', ctx=Load()),
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
                            left=Name(id='es_check', ctx=Load()),
                            ops=[Is()],
                            comparators=[Constant(value=None, kind=None)],
                        ),
                        Constant(value='es-check tool not found on this system', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
