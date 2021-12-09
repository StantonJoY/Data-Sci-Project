Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.website.tools',
            names=[alias(name='distance', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
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
        ClassDef(
            name='TestFuzzy',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_fuzzy_names',
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
                            targets=[Name(id='fields_per_model', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='website.page', kind=None)],
                                values=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='match_pattern', ctx=Store())],
                            value=Constant(value='\\w{4,}', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='words', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='model_name', ctx=Store()),
                                    Name(id='fields', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='fields_per_model', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='model_name', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='description', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='fields', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='description', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='model', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='description', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='model', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search_read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(elts=[], ctx=Load()),
                                            Name(id='fields', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=100, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='field', ctx=Store()),
                                                    Name(id='value', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='value', ctx=Load()),
                                                            Name(id='str', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='field', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='arch', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='view_arch', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='etree', ctx=Load()),
                                                                            attr='fromstring',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='value', ctx=Load()),
                                                                                    attr='encode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='utf-8', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='value', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Constant(value=' ', kind=None),
                                                                            attr='join',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='view_arch', ctx=Load()),
                                                                                    attr='itertext',
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
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        For(
                                                            target=Name(id='word', ctx=Store()),
                                                            iter=Call(
                                                                func=Attribute(
                                                                    value=Name(id='re', ctx=Load()),
                                                                    attr='findall',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='match_pattern', ctx=Load()),
                                                                    Name(id='value', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='words', ctx=Load()),
                                                                            attr='add',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='word', ctx=Load()),
                                                                                    attr='lower',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
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
                                                    orelse=[],
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
                                    Constant(value='%s words in target dictionary', kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='words', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.default_website', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='typos', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='add_typo',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='expected', annotation=None, type_comment=None),
                                    arg(arg='typo', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='typo', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='words', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='typos', ctx=Load()),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='typo', ctx=Load()),
                                                            Call(
                                                                func=Name(id='set', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='expected', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='search', ctx=Store()),
                            iter=Name(id='words', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='index', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=2, kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='search', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='search', ctx=Load()),
                                                    slice=Name(id='index', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='search', ctx=Load()),
                                                        slice=BinOp(
                                                            left=Name(id='index', ctx=Load()),
                                                            op=Sub(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='add_typo', ctx=Load()),
                                                        args=[
                                                            Name(id='search', ctx=Load()),
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=Subscript(
                                                                            value=Name(id='search', ctx=Load()),
                                                                            slice=Slice(
                                                                                lower=None,
                                                                                upper=BinOp(
                                                                                    left=Name(id='index', ctx=Load()),
                                                                                    op=Sub(),
                                                                                    right=Constant(value=1, kind=None),
                                                                                ),
                                                                                step=None,
                                                                            ),
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Subscript(
                                                                            value=Name(id='search', ctx=Load()),
                                                                            slice=Name(id='index', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Subscript(
                                                                        value=Name(id='search', ctx=Load()),
                                                                        slice=BinOp(
                                                                            left=Name(id='index', ctx=Load()),
                                                                            op=Sub(),
                                                                            right=Constant(value=1, kind=None),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Name(id='search', ctx=Load()),
                                                                    slice=Slice(
                                                                        lower=BinOp(
                                                                            left=Name(id='index', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value=1, kind=None),
                                                                        ),
                                                                        upper=None,
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='search', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=4, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='add_typo', ctx=Load()),
                                                        args=[
                                                            Name(id='search', ctx=Load()),
                                                            BinOp(
                                                                left=Subscript(
                                                                    value=Name(id='search', ctx=Load()),
                                                                    slice=Slice(
                                                                        lower=None,
                                                                        upper=BinOp(
                                                                            left=Name(id='index', ctx=Load()),
                                                                            op=Sub(),
                                                                            right=Constant(value=1, kind=None),
                                                                        ),
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Name(id='search', ctx=Load()),
                                                                    slice=Slice(
                                                                        lower=Name(id='index', ctx=Load()),
                                                                        upper=None,
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='add_typo', ctx=Load()),
                                                args=[
                                                    Name(id='search', ctx=Load()),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Name(id='search', ctx=Load()),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=BinOp(
                                                                        left=Name(id='index', ctx=Load()),
                                                                        op=Sub(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value='!', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Name(id='search', ctx=Load()),
                                                            slice=Slice(
                                                                lower=Name(id='index', ctx=Load()),
                                                                upper=None,
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='words', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[Name(id='words', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='words', ctx=Load()),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mismatch_count', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='search', ctx=Store()),
                                    Name(id='expected', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='typos', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fuzzy_guess', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='website', ctx=Load()),
                                            attr='_search_find_fuzzy_term',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(keys=[], values=[]),
                                            Name(id='search', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='word_list',
                                                value=Name(id='words', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='fuzzy_guess', ctx=Load()),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='fuzzy_guess', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='expected', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Name(id='fuzzy_guess', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            ListComp(
                                                                elt=Subscript(
                                                                    value=Name(id='exp', ctx=Load()),
                                                                    slice=Slice(
                                                                        lower=None,
                                                                        upper=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Constant(value=1, kind=None),
                                                                        ),
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='exp', ctx=Store()),
                                                                        iter=Name(id='expected', ctx=Load()),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='mismatch_count', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value="'%s' fuzzy matched to '%s' instead of %s", kind=None),
                                                    Name(id='search', ctx=Load()),
                                                    Name(id='fuzzy_guess', ctx=Load()),
                                                    Name(id='expected', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ratio', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value=100.0, kind=None),
                                    op=Mult(),
                                    right=Name(id='mismatch_count', ctx=Load()),
                                ),
                                op=Div(),
                                right=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='typos', ctx=Load())],
                                    keywords=[],
                                ),
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
                                    Constant(value='%s wrong guesses over %s tested typos (%.2f%%)', kind=None),
                                    Name(id='mismatch_count', ctx=Load()),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='typos', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='ratio', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='typos', ctx=Load()),
                                    attr='clear',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='words', ctx=Load()),
                                    attr='clear',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        left=Name(id='ratio', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Constant(value='Too many wrong fuzzy guesses', kind=None),
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
                    name='test_02_distance',
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='gravity', kind=None),
                                            Constant(value='granity', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='gravity', kind=None),
                                            Constant(value='graity', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='gravity', kind=None),
                                            Constant(value='grait', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='gravity', kind=None),
                                            Constant(value='griaty', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='gravity', kind=None),
                                            Constant(value='giraty', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='gravity', kind=None),
                                            Constant(value='giraty', kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
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
                                    Call(
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='gravity', kind=None),
                                            Constant(value='girafe', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
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
                                    Call(
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='warranty', kind=None),
                                            Constant(value='warantl', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='warranty', kind=None),
                                            Constant(value='warranty', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='', kind=None),
                                            Constant(value='warranty', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
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
                                    Call(
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='', kind=None),
                                            Constant(value='warranty', kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=8, kind=None),
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='warranty', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=8, kind=None),
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
                                        func=Name(id='distance', ctx=Load()),
                                        args=[
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
