Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='fnmatch', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Assign(
            targets=[Name(id='j', ctx=Store())],
            value=Attribute(
                value=Attribute(
                    value=Name(id='os', ctx=Load()),
                    attr='path',
                    ctx=Load(),
                ),
                attr='join',
                ctx=Load(),
            ),
            type_comment=None,
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
            module='odoo.tests',
            names=[alias(name='BaseCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='LintCase',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Utility method for lint-type cases\n    ', kind=None),
                ),
                FunctionDef(
                    name='iter_module_files',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='globs', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Yields the paths of all the module files matching the provided globs\n        (AND-ed)\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='modroot', ctx=Store()),
                            iter=Call(
                                func=Name(id='map', ctx=Load()),
                                args=[
                                    Name(id='get_module_path', ctx=Load()),
                                    Call(
                                        func=Name(id='get_modules', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='root', ctx=Store()),
                                            Name(id='_', ctx=Store()),
                                            Name(id='fnames', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='walk',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='modroot', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='fnames', ctx=Store())],
                                            value=ListComp(
                                                elt=Call(
                                                    func=Name(id='j', ctx=Load()),
                                                    args=[
                                                        Name(id='root', ctx=Load()),
                                                        Name(id='n', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='n', ctx=Store()),
                                                        iter=Name(id='fnames', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='glob', ctx=Store()),
                                            iter=Name(id='globs', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='fnames', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='fnmatch', ctx=Load()),
                                                            attr='filter',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='fnames', ctx=Load()),
                                                            Name(id='glob', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=YieldFrom(
                                                value=Name(id='fnames', ctx=Load()),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='NodeVisitor',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Simple NodeVisitor.', kind=None),
                ),
                FunctionDef(
                    name='visit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='node', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='method', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='visit_', kind=None),
                                op=Add(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='node', ctx=Load()),
                                        attr='__class__',
                                        ctx=Load(),
                                    ),
                                    attr='__name__',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='visitor', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='method', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='generic_visit',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='visitor', ctx=Load()),
                                args=[Name(id='node', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='generic_visit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='node', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='child', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='ast', ctx=Load()),
                                    attr='iter_child_nodes',
                                    ctx=Load(),
                                ),
                                args=[Name(id='node', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=YieldFrom(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='visit',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='child', ctx=Load())],
                                            keywords=[],
                                        ),
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
