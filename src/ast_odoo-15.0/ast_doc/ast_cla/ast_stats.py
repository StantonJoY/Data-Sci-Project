Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='glob', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        Assign(
            targets=[Name(id='cla_glob', ctx=Store())],
            value=Constant(value='doc/cla/*/*.md', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='cla', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Constant(value='', kind=None),
                    attr='join',
                    ctx=Load(),
                ),
                args=[
                    GeneratorExp(
                        elt=Call(
                            func=Attribute(
                                value=Call(
                                    func=Name(id='open', ctx=Load()),
                                    args=[Name(id='f', ctx=Load())],
                                    keywords=[],
                                ),
                                attr='read',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='f', ctx=Store()),
                                iter=Call(
                                    func=Attribute(
                                        value=Name(id='glob', ctx=Load()),
                                        attr='glob',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='cla_glob', ctx=Load())],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='cla', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='cla', ctx=Load()),
                    attr='lower',
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='cla_signed',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='email', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='match',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='.*(odoo|openerp|tinyerp).com$', kind=None),
                            Name(id='email', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Attribute(
                                value=Name(id='cla', ctx=Load()),
                                attr='find',
                                ctx=Load(),
                            ),
                            args=[Name(id='email', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[NotEq()],
                        comparators=[
                            UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value=False, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='blamestat',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='ext', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='py', kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='r', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ok', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='okl', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ko', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='kol', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='p', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='Popen',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Constant(value="git ls-tree -r -z --name-only HEAD | grep -z '.%s$' | xargs -0 -n1 git blame --line-porcelain HEAD |grep  '^author-mail ' |sort |uniq -c|sort -nr", kind=None),
                                op=Mod(),
                                right=Name(id='ext', ctx=Load()),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='shell',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='stdout',
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
                For(
                    target=Name(id='i', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='p', ctx=Load()),
                                        attr='stdout',
                                        ctx=Load(),
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='\n', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(\\d+) author-mail <([^ @<]+@[^ @<]+)>', kind=None),
                                    Name(id='i', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mo', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='lines', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='mo', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=1, kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='email', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mo', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='cla_signed', ctx=Load()),
                                        args=[Name(id='email', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='ok', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='lines', ctx=Load()),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='okl', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='i', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Name(id='ko', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='lines', ctx=Load()),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='kol', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='i', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            BinOp(
                                left=Constant(value='-', kind=None),
                                op=Mult(),
                                right=Constant(value=60, kind=None),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            Constant(value='Stats for ', kind=None),
                            Name(id='ext', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            BinOp(
                                left=Constant(value='-', kind=None),
                                op=Mult(),
                                right=Constant(value=60, kind=None),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            BinOp(
                                left=Constant(value='\nCLA SIGNED %s/%s (%.0f%%)', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='ok', ctx=Load()),
                                        BinOp(
                                            left=Name(id='ok', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='ko', ctx=Load()),
                                        ),
                                        BinOp(
                                            left=BinOp(
                                                left=Name(id='ok', ctx=Load()),
                                                op=Mult(),
                                                right=Constant(value=100.0, kind=None),
                                            ),
                                            op=Div(),
                                            right=BinOp(
                                                left=Name(id='ok', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='ko', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                For(
                    target=Name(id='i', ctx=Store()),
                    iter=Name(id='okl', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[Name(id='i', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            BinOp(
                                left=Constant(value='\nCLA MISSING %s/%s (%.0f%%)\n', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='ko', ctx=Load()),
                                        BinOp(
                                            left=Name(id='ok', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='ko', ctx=Load()),
                                        ),
                                        BinOp(
                                            left=BinOp(
                                                left=Name(id='ko', ctx=Load()),
                                                op=Mult(),
                                                right=Constant(value=100.0, kind=None),
                                            ),
                                            op=Div(),
                                            right=BinOp(
                                                left=Name(id='ok', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='ko', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                For(
                    target=Name(id='i', ctx=Store()),
                    iter=Name(id='kol', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[Name(id='i', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Expr(
            value=Call(
                func=Name(id='blamestat', ctx=Load()),
                args=[Constant(value='md', kind=None)],
                keywords=[],
            ),
        ),
        Expr(
            value=Call(
                func=Name(id='blamestat', ctx=Load()),
                args=[Constant(value='rst', kind=None)],
                keywords=[],
            ),
        ),
        Expr(
            value=Call(
                func=Name(id='blamestat', ctx=Load()),
                args=[Constant(value='py', kind=None)],
                keywords=[],
            ),
        ),
        Expr(
            value=Call(
                func=Name(id='blamestat', ctx=Load()),
                args=[Constant(value='js', kind=None)],
                keywords=[],
            ),
        ),
        Expr(
            value=Call(
                func=Name(id='blamestat', ctx=Load()),
                args=[Constant(value='xml', kind=None)],
                keywords=[],
            ),
        ),
        Expr(
            value=Call(
                func=Name(id='blamestat', ctx=Load()),
                args=[Constant(value='csv', kind=None)],
                keywords=[],
            ),
        ),
    ],
    type_ignores=[],
)
