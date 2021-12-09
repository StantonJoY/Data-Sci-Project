Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='collections', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='socket', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='email.utils',
            names=[alias(name='getaddresses', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='urllib.parse',
            names=[alias(name='urlparse', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='idna', asname=None)],
        ),
        Import(
            names=[alias(name='markupsafe', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml.html',
            names=[alias(name='clean', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.loglevels',
            names=[alias(name='ustr', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='misc', asname=None)],
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
        Assign(
            targets=[Name(id='tags_to_kill', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='base', kind=None),
                    Constant(value='embed', kind=None),
                    Constant(value='frame', kind=None),
                    Constant(value='head', kind=None),
                    Constant(value='iframe', kind=None),
                    Constant(value='link', kind=None),
                    Constant(value='meta', kind=None),
                    Constant(value='noscript', kind=None),
                    Constant(value='object', kind=None),
                    Constant(value='script', kind=None),
                    Constant(value='style', kind=None),
                    Constant(value='title', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='tags_to_remove', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='html', kind=None),
                    Constant(value='body', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='allowed_tags', ctx=Store())],
            value=BinOp(
                left=Attribute(
                    value=Attribute(
                        value=Name(id='clean', ctx=Load()),
                        attr='defs',
                        ctx=Load(),
                    ),
                    attr='tags',
                    ctx=Load(),
                ),
                op=BitOr(),
                right=Call(
                    func=Name(id='frozenset', ctx=Load()),
                    args=[
                        BinOp(
                            left=Call(
                                func=Attribute(
                                    value=Constant(value='article bdi section header footer hgroup nav aside figure main', kind=None),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            op=Add(),
                            right=List(
                                elts=[
                                    Attribute(
                                        value=Name(id='etree', ctx=Load()),
                                        attr='Comment',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    keywords=[],
                ),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='safe_attrs', ctx=Store())],
            value=BinOp(
                left=Attribute(
                    value=Attribute(
                        value=Name(id='clean', ctx=Load()),
                        attr='defs',
                        ctx=Load(),
                    ),
                    attr='safe_attrs',
                    ctx=Load(),
                ),
                op=BitOr(),
                right=Call(
                    func=Name(id='frozenset', ctx=Load()),
                    args=[
                        List(
                            elts=[
                                Constant(value='style', kind=None),
                                Constant(value='data-o-mail-quote', kind=None),
                                Constant(value='data-oe-model', kind=None),
                                Constant(value='data-oe-id', kind=None),
                                Constant(value='data-oe-field', kind=None),
                                Constant(value='data-oe-type', kind=None),
                                Constant(value='data-oe-expression', kind=None),
                                Constant(value='data-oe-translation-id', kind=None),
                                Constant(value='data-oe-nodeid', kind=None),
                                Constant(value='data-publish', kind=None),
                                Constant(value='data-id', kind=None),
                                Constant(value='data-res_id', kind=None),
                                Constant(value='data-interval', kind=None),
                                Constant(value='data-member_id', kind=None),
                                Constant(value='data-scroll-background-ratio', kind=None),
                                Constant(value='data-view-id', kind=None),
                                Constant(value='data-class', kind=None),
                                Constant(value='data-mimetype', kind=None),
                                Constant(value='data-original-src', kind=None),
                                Constant(value='data-original-id', kind=None),
                                Constant(value='data-gl-filter', kind=None),
                                Constant(value='data-quality', kind=None),
                                Constant(value='data-resize-width', kind=None),
                                Constant(value='data-shape', kind=None),
                                Constant(value='data-shape-colors', kind=None),
                                Constant(value='data-file-name', kind=None),
                                Constant(value='data-original-mimetype', kind=None),
                            ],
                            ctx=Load(),
                        ),
                    ],
                    keywords=[],
                ),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='_Cleaner',
            bases=[
                Attribute(
                    value=Name(id='clean', ctx=Load()),
                    attr='Cleaner',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_style_re', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='([\\w-]+)\\s*:\\s*((?:[^;"\']|"[^";]*"|\'[^\';]*\')+)', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_style_whitelist', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='font-size', kind=None),
                            Constant(value='font-family', kind=None),
                            Constant(value='font-weight', kind=None),
                            Constant(value='background-color', kind=None),
                            Constant(value='color', kind=None),
                            Constant(value='text-align', kind=None),
                            Constant(value='line-height', kind=None),
                            Constant(value='letter-spacing', kind=None),
                            Constant(value='text-transform', kind=None),
                            Constant(value='text-decoration', kind=None),
                            Constant(value='opacity', kind=None),
                            Constant(value='float', kind=None),
                            Constant(value='vertical-align', kind=None),
                            Constant(value='display', kind=None),
                            Constant(value='padding', kind=None),
                            Constant(value='padding-top', kind=None),
                            Constant(value='padding-left', kind=None),
                            Constant(value='padding-bottom', kind=None),
                            Constant(value='padding-right', kind=None),
                            Constant(value='margin', kind=None),
                            Constant(value='margin-top', kind=None),
                            Constant(value='margin-left', kind=None),
                            Constant(value='margin-bottom', kind=None),
                            Constant(value='margin-right', kind=None),
                            Constant(value='white-space', kind=None),
                            Constant(value='border', kind=None),
                            Constant(value='border-color', kind=None),
                            Constant(value='border-radius', kind=None),
                            Constant(value='border-style', kind=None),
                            Constant(value='border-width', kind=None),
                            Constant(value='border-top', kind=None),
                            Constant(value='border-bottom', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                            Constant(value='max-width', kind=None),
                            Constant(value='min-width', kind=None),
                            Constant(value='min-height', kind=None),
                            Constant(value='border-collapse', kind=None),
                            Constant(value='border-spacing', kind=None),
                            Constant(value='caption-side', kind=None),
                            Constant(value='empty-cells', kind=None),
                            Constant(value='table-layout', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_style_whitelist', ctx=Load()),
                            attr='extend',
                            ctx=Load(),
                        ),
                        args=[
                            ListComp(
                                elt=BinOp(
                                    left=Constant(value='border-%s-%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Name(id='position', ctx=Load()),
                                            Name(id='attribute', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='position', ctx=Store()),
                                        iter=List(
                                            elts=[
                                                Constant(value='top', kind=None),
                                                Constant(value='bottom', kind=None),
                                                Constant(value='left', kind=None),
                                                Constant(value='right', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                    comprehension(
                                        target=Name(id='attribute', ctx=Store()),
                                        iter=Tuple(
                                            elts=[
                                                Constant(value='style', kind=None),
                                                Constant(value='color', kind=None),
                                                Constant(value='width', kind=None),
                                                Constant(value='left-radius', kind=None),
                                                Constant(value='right-radius', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='strip_classes', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sanitize_style', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='doc', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='el', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='doc', ctx=Load()),
                                    attr='iter',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tag',
                                        value=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='Element',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tag_quote',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='el', ctx=Load())],
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='_Cleaner', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__call__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='doc', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='self', ctx=Load()),
                                                Constant(value='safe_attrs_only', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='strip_classes',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='el', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='doc', ctx=Load()),
                                            attr='iter',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tag',
                                                value=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='Element',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='strip_class',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='el', ctx=Load())],
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='style',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sanitize_style',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='el', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='doc', ctx=Load()),
                                            attr='iter',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tag',
                                                value=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='Element',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='parse_style',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='el', ctx=Load())],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='tag_quote',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='_create_new_node',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='tag', annotation=None, type_comment=None),
                                    arg(arg='text', annotation=None, type_comment=None),
                                    arg(arg='tail', annotation=None, type_comment=None),
                                    arg(arg='attrs', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_node', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='Element',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tag', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='new_node', ctx=Load()),
                                            attr='text',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='text', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='new_node', ctx=Load()),
                                            attr='tail',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='tail', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='attrs', ctx=Load()),
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='key', ctx=Store()),
                                                    Name(id='val', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='attrs', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='new_node', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='key', ctx=Load()),
                                                            Name(id='val', ctx=Load()),
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
                                Return(
                                    value=Name(id='new_node', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_tag_matching_regex_in_text',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='regex', annotation=None, type_comment=None),
                                    arg(arg='node', annotation=None, type_comment=None),
                                    arg(arg='tag', annotation=None, type_comment=None),
                                    arg(arg='attrs', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value='span', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='text', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='re', ctx=Load()),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='regex', ctx=Load()),
                                                Name(id='text', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[Return(value=None)],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='child_node', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='idx', ctx=Store()),
                                                Name(id='node_idx', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='item', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='finditer',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='regex', ctx=Load()),
                                            Name(id='text', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='new_node', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_create_new_node', ctx=Load()),
                                                args=[
                                                    Name(id='tag', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='text', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Call(
                                                                func=Attribute(
                                                                    value=Name(id='item', ctx=Load()),
                                                                    attr='start',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            upper=Call(
                                                                func=Attribute(
                                                                    value=Name(id='item', ctx=Load()),
                                                                    attr='end',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=None, kind=None),
                                                    Name(id='attrs', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='child_node', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='text',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='text', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Name(id='idx', ctx=Load()),
                                                            upper=Call(
                                                                func=Attribute(
                                                                    value=Name(id='item', ctx=Load()),
                                                                    attr='start',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='new_node', ctx=Load()),
                                                            attr='tail',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='text', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Call(
                                                                func=Attribute(
                                                                    value=Name(id='item', ctx=Load()),
                                                                    attr='end',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='insert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='node_idx', ctx=Load()),
                                                            Name(id='new_node', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='child_node', ctx=Load()),
                                                            attr='tail',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='text', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Name(id='idx', ctx=Load()),
                                                            upper=Call(
                                                                func=Attribute(
                                                                    value=Name(id='item', ctx=Load()),
                                                                    attr='start',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='new_node', ctx=Load()),
                                                            attr='tail',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='text', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Call(
                                                                func=Attribute(
                                                                    value=Name(id='item', ctx=Load()),
                                                                    attr='end',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='insert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='node_idx', ctx=Load()),
                                                            Name(id='new_node', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='child_node', ctx=Store())],
                                            value=Name(id='new_node', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='idx', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='item', ctx=Load()),
                                                    attr='end',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='node_idx', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='node_idx', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
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
                        Assign(
                            targets=[Name(id='el_class', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='class', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='el_id', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='id', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='gmail_extra', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='el_class', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='divRplyFwdMsg', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='el_id', ctx=Load())],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Constant(value='SkyDrivePlaceholder', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='el_class', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='SkyDrivePlaceholder', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='el_class', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='data-o-mail-quote', kind=None),
                                            Constant(value='1', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='getparent',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='getparent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='data-o-mail-quote-container', kind=None),
                                                    Constant(value='1', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='el', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='hr', kind=None)],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Constant(value='stopSpelling', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='el_class', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Constant(value='stopSpelling', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='el_id', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Constant(value='yahoo_quoted', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='el_class', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='data-o-mail-quote', kind=None),
                                            Constant(value='1', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='sibling', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='itersiblings',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='preceding',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sibling', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='data-o-mail-quote', kind=None),
                                                    Constant(value='1', kind=None),
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
                        Assign(
                            targets=[Name(id='signature_begin', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='compile',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='((?:(?:^|\\n)[-]{2}[\\s]?$))', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='find',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='br', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='signature_begin', ctx=Load()),
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='data-o-mail-quote', kind=None),
                                            Constant(value='1', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='getparent',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='getparent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='data-o-mail-quote-container', kind=None),
                                                    Constant(value='1', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='text_complete_regex', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='compile',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='((?:\\n[>]+[^\\n\\r]*)+|(?:(?:^|\\n)[-]{2}[\\s]?[\\r\\n]{1,2}[\\s\\S]+))', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='data-o-mail-quote', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_tag_matching_regex_in_text', ctx=Load()),
                                        args=[
                                            Name(id='text_complete_regex', ctx=Load()),
                                            Name(id='el', ctx=Load()),
                                            Constant(value='span', kind=None),
                                            Dict(
                                                keys=[Constant(value='data-o-mail-quote', kind=None)],
                                                values=[Constant(value='1', kind=None)],
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
                                left=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='tag',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='blockquote', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='data-o-mail-quote-node', kind=None),
                                            Constant(value='1', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='data-o-mail-quote', kind=None),
                                            Constant(value='1', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='getparent',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='getparent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='data-o-mail-quote', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='getparent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='data-o-mail-quote-container', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='getparent',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='data-o-mail-quote-node', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='data-o-mail-quote', kind=None),
                                            Constant(value='1', kind=None),
                                        ],
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
                FunctionDef(
                    name='strip_class',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                        ],
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
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='class', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='class', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='parse_style',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='attributes', ctx=Store())],
                            value=Attribute(
                                value=Name(id='el', ctx=Load()),
                                attr='attrib',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='styling', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attributes', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='style', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='styling', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='valid_styles', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='collections', ctx=Load()),
                                            attr='OrderedDict',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='styles', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_style_re',
                                                ctx=Load(),
                                            ),
                                            attr='findall',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='styling', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='style', ctx=Store()),
                                    iter=Name(id='styles', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='style', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='lower',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_style_whitelist',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='valid_styles', ctx=Load()),
                                                            slice=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='style', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='lower',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='style', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='valid_styles', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='style', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value='; ', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    GeneratorExp(
                                                        elt=BinOp(
                                                            left=Constant(value='%s:%s', kind=None),
                                                            op=Mod(),
                                                            right=Tuple(
                                                                elts=[
                                                                    Name(id='key', ctx=Load()),
                                                                    Name(id='val', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Tuple(
                                                                    elts=[
                                                                        Name(id='key', ctx=Store()),
                                                                        Name(id='val', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='valid_styles', ctx=Load()),
                                                                        attr='items',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
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
                                    ],
                                    orelse=[
                                        Delete(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='style', kind=None),
                                                    ctx=Del(),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='html_sanitize',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='src', annotation=None, type_comment=None),
                    arg(arg='silent', annotation=None, type_comment=None),
                    arg(arg='sanitize_tags', annotation=None, type_comment=None),
                    arg(arg='sanitize_attributes', annotation=None, type_comment=None),
                    arg(arg='sanitize_style', annotation=None, type_comment=None),
                    arg(arg='sanitize_form', annotation=None, type_comment=None),
                    arg(arg='strip_style', annotation=None, type_comment=None),
                    arg(arg='strip_classes', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=True, kind=None),
                    Constant(value=True, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=True, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='src', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Name(id='src', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='src', ctx=Store())],
                    value=Call(
                        func=Name(id='ustr', ctx=Load()),
                        args=[Name(id='src', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='errors',
                                value=Constant(value='replace', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='doctype', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='(<[^>]*\\s)(encoding=(["\\\'][^"\\\']*?["\\\']|[^\\s\\n\\r>]+)(\\s[^>]*|/)?>)', kind=None),
                            BinOp(
                                left=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='IGNORECASE',
                                    ctx=Load(),
                                ),
                                op=BitOr(),
                                right=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='DOTALL',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='src', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='doctype', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='', kind='u'),
                            Name(id='src', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='logger', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='logging', ctx=Load()),
                            attr='getLogger',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Name(id='__name__', ctx=Load()),
                                op=Add(),
                                right=Constant(value='.html_sanitize', kind=None),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='src', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='src', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='<%', kind='u'),
                            Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='html_escape',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='<%', kind='u')],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='src', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='src', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='%>', kind='u'),
                            Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='html_escape',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='%>', kind='u')],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='kwargs', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='page_structure', kind=None),
                            Constant(value='style', kind=None),
                            Constant(value='sanitize_style', kind=None),
                            Constant(value='forms', kind=None),
                            Constant(value='remove_unknown_tags', kind=None),
                            Constant(value='comments', kind=None),
                            Constant(value='processing_instructions', kind=None),
                        ],
                        values=[
                            Constant(value=True, kind=None),
                            Name(id='strip_style', ctx=Load()),
                            Name(id='sanitize_style', ctx=Load()),
                            Name(id='sanitize_form', ctx=Load()),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='sanitize_tags', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='kwargs', ctx=Load()),
                                    slice=Constant(value='allow_tags', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='allowed_tags', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='LXML_VERSION',
                                    ctx=Load(),
                                ),
                                ops=[GtE()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=2, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='kill_tags', kind=None),
                                                    Constant(value='remove_tags', kind=None),
                                                ],
                                                values=[
                                                    Name(id='tags_to_kill', ctx=Load()),
                                                    Name(id='tags_to_remove', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='remove_tags', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Name(id='tags_to_kill', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='tags_to_remove', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='sanitize_attributes', ctx=Load()),
                            Compare(
                                left=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='LXML_VERSION',
                                    ctx=Load(),
                                ),
                                ops=[GtE()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        If(
                            test=Name(id='strip_classes', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='current_safe_attrs', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='safe_attrs', ctx=Load()),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='frozenset', ctx=Load()),
                                            args=[
                                                List(
                                                    elts=[Constant(value='class', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='current_safe_attrs', ctx=Store())],
                                    value=Name(id='safe_attrs', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='safe_attrs_only', kind=None),
                                            Constant(value='safe_attrs', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Name(id='current_safe_attrs', ctx=Load()),
                                        ],
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
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='safe_attrs_only', kind=None),
                                            Constant(value='strip_classes', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Name(id='strip_classes', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='cleaner', ctx=Store())],
                            value=Call(
                                func=Name(id='_Cleaner', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaner', ctx=Load()),
                                    attr='clean_html',
                                    ctx=Load(),
                                ),
                                args=[Name(id='src', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='cleaned', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%24', kind='u'),
                                    Constant(value='$', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%7B', kind='u'),
                                    Constant(value='{', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%7D', kind='u'),
                                    Constant(value='}', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%20', kind='u'),
                                    Constant(value=' ', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%5B', kind='u'),
                                    Constant(value='[', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%5D', kind='u'),
                                    Constant(value=']', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%7C', kind='u'),
                                    Constant(value='|', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='&lt;%', kind='u'),
                                    Constant(value='<%', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%&gt;', kind='u'),
                                    Constant(value='%>', kind='u'),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\xa0', kind='u'),
                                    Constant(value='&nbsp;', kind='u'),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Name(id='etree', ctx=Load()),
                                attr='ParserError',
                                ctx=Load(),
                            ),
                            name='e',
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='empty', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value='', kind='u'),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='silent', ctx=Load()),
                                    ),
                                    body=[Raise(exc=None, cause=None)],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='ParserError obtained when sanitizing %r', kind='u'),
                                            Name(id='src', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='exc_info',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='cleaned', ctx=Store())],
                                    value=Constant(value='<p>ParserError when sanitizing</p>', kind='u'),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name=None,
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='silent', ctx=Load()),
                                    ),
                                    body=[Raise(exc=None, cause=None)],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='unknown error obtained when sanitizing %r', kind='u'),
                                            Name(id='src', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='exc_info',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='cleaned', ctx=Store())],
                                    value=Constant(value='<p>Unknown error when sanitizing</p>', kind='u'),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='<div>', kind='u')],
                                keywords=[],
                            ),
                            Call(
                                func=Attribute(
                                    value=Name(id='cleaned', ctx=Load()),
                                    attr='endswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='</div>', kind='u')],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cleaned', ctx=Store())],
                            value=Subscript(
                                value=Name(id='cleaned', ctx=Load()),
                                slice=Slice(
                                    lower=Constant(value=5, kind=None),
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=6, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='markupsafe', ctx=Load()),
                            attr='Markup',
                            ctx=Load(),
                        ),
                        args=[Name(id='cleaned', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='URL_REGEX', ctx=Store())],
            value=Constant(value='(\\bhref=[\\\'"](?!mailto:|tel:|sms:)([^\\\'"]+)[\\\'"])', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TEXT_URL_REGEX', ctx=Store())],
            value=Constant(value='https?://[a-zA-Z0-9@:%._\\+~#=/-]+(?:\\?\\S+)?', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='HTML_TAG_URL_REGEX', ctx=Store())],
            value=BinOp(
                left=Name(id='URL_REGEX', ctx=Load()),
                op=Add(),
                right=Constant(value='([^<>]*>([^<>]+)<\\/)?', kind=None),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='validate_url',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='url', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Compare(
                        left=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urls', ctx=Load()),
                                    attr='url_parse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[],
                            ),
                            attr='scheme',
                            ctx=Load(),
                        ),
                        ops=[NotIn()],
                        comparators=[
                            Tuple(
                                elts=[
                                    Constant(value='http', kind=None),
                                    Constant(value='https', kind=None),
                                    Constant(value='ftp', kind=None),
                                    Constant(value='ftps', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Constant(value='http://', kind=None),
                                op=Add(),
                                right=Name(id='url', ctx=Load()),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='url', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='is_html_empty',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='html_content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Check if a html content is empty. If there are only formatting tags with style\n    attributes or a void content  return True. Famous use case if a\n    \'<p style="..."><br></p>\' added by some web editor.\n\n    :param str html_content: html content, coming from example from an HTML field\n    :returns: bool, True if no content found or if containing only void formatting tags\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='html_content', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='tag_re', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='\\<\\s*\\/?(?:p|div|span|br|b|i|font)(?:(?=\\s+\\w*)[^/>]*|\\s*)/?\\s*\\>', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='bool', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='re', ctx=Load()),
                                                attr='sub',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='tag_re', ctx=Load()),
                                                Constant(value='', kind=None),
                                                Name(id='html_content', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='strip',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='html_keep_url',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='text', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Transform the url into clickable link with <a/> tag ', kind=None),
                ),
                Assign(
                    targets=[Name(id='idx', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='final', ctx=Store())],
                    value=Constant(value='', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='link_tags', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='(?<!["\'])((ftp|http|https):\\/\\/(\\w+:{0,1}\\w*@)?([^\\s<"\']+)(:[0-9]+)?(\\/|\\/([^\\s<"\']))?)(?![^\\s<"\']*["\']|[^\\s<"\']*</a>)', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='item', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='finditer',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='link_tags', ctx=Load()),
                            Name(id='text', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        AugAssign(
                            target=Name(id='final', ctx=Store()),
                            op=Add(),
                            value=Subscript(
                                value=Name(id='text', ctx=Load()),
                                slice=Slice(
                                    lower=Name(id='idx', ctx=Load()),
                                    upper=Call(
                                        func=Attribute(
                                            value=Name(id='item', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                        ),
                        AugAssign(
                            target=Name(id='final', ctx=Store()),
                            op=Add(),
                            value=BinOp(
                                left=Constant(value='<a href="%s" target="_blank" rel="noreferrer noopener">%s</a>', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='item', ctx=Load()),
                                                attr='group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='item', ctx=Load()),
                                                attr='group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='idx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='item', ctx=Load()),
                                    attr='end',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                AugAssign(
                    target=Name(id='final', ctx=Store()),
                    op=Add(),
                    value=Subscript(
                        value=Name(id='text', ctx=Load()),
                        slice=Slice(
                            lower=Name(id='idx', ctx=Load()),
                            upper=None,
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                ),
                Return(
                    value=Name(id='final', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='html2plaintext',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='html', annotation=None, type_comment=None),
                    arg(arg='body_id', annotation=None, type_comment=None),
                    arg(arg='encoding', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value='utf-8', kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' From an HTML text, convert the HTML to plain text.\n    If @param body_id is provided then this is the tag where the\n    body (not necessarily <body>) starts.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Name(id='ustr', ctx=Load()),
                        args=[Name(id='html', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Attribute(
                                value=Name(id='html', ctx=Load()),
                                attr='strip',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Return(
                            value=Constant(value='', kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='tree', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='fromstring',
                            ctx=Load(),
                        ),
                        args=[Name(id='html', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='parser',
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='etree', ctx=Load()),
                                        attr='HTMLParser',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='body_id', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='//*[@id=%s]', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[Name(id='body_id', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//body', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                If(
                    test=Call(
                        func=Name(id='len', ctx=Load()),
                        args=[Name(id='source', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tree', ctx=Store())],
                            value=Subscript(
                                value=Name(id='source', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='url_index', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='i', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                For(
                    target=Name(id='link', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='tree', ctx=Load()),
                            attr='findall',
                            ctx=Load(),
                        ),
                        args=[Constant(value='.//a', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='link', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='href', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='url', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='i', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='link', ctx=Load()),
                                            attr='tag',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='span', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='link', ctx=Load()),
                                            attr='text',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s [%s]', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='link', ctx=Load()),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                                Name(id='i', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='url_index', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='url', ctx=Load())],
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
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Name(id='ustr', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='tostring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tree', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='encoding',
                                        value=Name(id='encoding', ctx=Load()),
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='&#13;', kind=None),
                            Constant(value='', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<strong>', kind=None),
                                    Constant(value='*', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='</strong>', kind=None),
                            Constant(value='*', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<b>', kind=None),
                                    Constant(value='*', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='</b>', kind=None),
                            Constant(value='*', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<h3>', kind=None),
                                    Constant(value='*', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='</h3>', kind=None),
                            Constant(value='*', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<h2>', kind=None),
                                    Constant(value='**', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='</h2>', kind=None),
                            Constant(value='**', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<h1>', kind=None),
                                    Constant(value='**', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='</h1>', kind=None),
                            Constant(value='**', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<em>', kind=None),
                                    Constant(value='/', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='</em>', kind=None),
                            Constant(value='/', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='<tr>', kind=None),
                            Constant(value='\n', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='</p>', kind=None),
                            Constant(value='\n', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='<br\\s*/?>', kind=None),
                            Constant(value='\n', kind=None),
                            Name(id='html', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='<.*?>', kind=None),
                            Constant(value=' ', kind=None),
                            Name(id='html', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Constant(value=' ', kind=None),
                                op=Mult(),
                                right=Constant(value=2, kind=None),
                            ),
                            Constant(value=' ', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='&gt;', kind=None),
                            Constant(value='>', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='&lt;', kind=None),
                            Constant(value='<', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='&amp;', kind=None),
                            Constant(value='&', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='\n', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='x', ctx=Load()),
                                        attr='strip',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='html', ctx=Load()),
                                                attr='splitlines',
                                                ctx=Load(),
                                            ),
                                            args=[],
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
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Constant(value='\n', kind=None),
                                op=Mult(),
                                right=Constant(value=2, kind=None),
                            ),
                            Constant(value='\n', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='i', ctx=Store()),
                            Name(id='url', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Name(id='enumerate', ctx=Load()),
                        args=[Name(id='url_index', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='i', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='html', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='\n\n', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='html', ctx=Store()),
                            op=Add(),
                            value=BinOp(
                                left=Call(
                                    func=Name(id='ustr', ctx=Load()),
                                    args=[Constant(value='[%s] %s\n', kind=None)],
                                    keywords=[],
                                ),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        BinOp(
                                            left=Name(id='i', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                        Name(id='url', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='strip',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='plaintext2html',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='text', annotation=None, type_comment=None),
                    arg(arg='container_tag', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Convert plaintext into html. Content of the text is escaped to manage\n        html entities, using misc.html_escape().\n        - all \n,\r are replaced by <br />\n        - enclose content into <p>\n        - convert url into clickable link\n        - 2 or more consecutive <br /> are considered as paragraph breaks\n\n        :param string container_tag: container of the html; by default the\n            content is embedded into a <div>\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='text', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='misc', ctx=Load()),
                            attr='html_escape',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Name(id='ustr', ctx=Load()),
                                args=[Name(id='text', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='text', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='(\\r\\n|\\r|\\n)', kind=None),
                            Constant(value='<br/>', kind=None),
                            Name(id='text', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='text', ctx=Store())],
                    value=Call(
                        func=Name(id='html_keep_url', ctx=Load()),
                        args=[Name(id='text', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='idx', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='final', ctx=Store())],
                    value=Constant(value='<p>', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='br_tags', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='(([<]\\s*[bB][rR]\\s*/?[>]\\s*){2,})', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='item', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='finditer',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='br_tags', ctx=Load()),
                            Name(id='text', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        AugAssign(
                            target=Name(id='final', ctx=Store()),
                            op=Add(),
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='text', ctx=Load()),
                                    slice=Slice(
                                        lower=Name(id='idx', ctx=Load()),
                                        upper=Call(
                                            func=Attribute(
                                                value=Name(id='item', ctx=Load()),
                                                attr='start',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Constant(value='</p><p>', kind=None),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='idx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='item', ctx=Load()),
                                    attr='end',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                AugAssign(
                    target=Name(id='final', ctx=Store()),
                    op=Add(),
                    value=BinOp(
                        left=Subscript(
                            value=Name(id='text', ctx=Load()),
                            slice=Slice(
                                lower=Name(id='idx', ctx=Load()),
                                upper=None,
                                step=None,
                            ),
                            ctx=Load(),
                        ),
                        op=Add(),
                        right=Constant(value='</p>', kind=None),
                    ),
                ),
                If(
                    test=Name(id='container_tag', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='final', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='<%s>%s</%s>', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='container_tag', ctx=Load()),
                                        Name(id='final', ctx=Load()),
                                        Name(id='container_tag', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='markupsafe', ctx=Load()),
                            attr='Markup',
                            ctx=Load(),
                        ),
                        args=[Name(id='final', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='append_content_to_html',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='html', annotation=None, type_comment=None),
                    arg(arg='content', annotation=None, type_comment=None),
                    arg(arg='plaintext', annotation=None, type_comment=None),
                    arg(arg='preserve', annotation=None, type_comment=None),
                    arg(arg='container_tag', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=True, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=" Append extra content at the end of an HTML snippet, trying\n        to locate the end of the HTML document (</body>, </html>, or\n        EOF), and converting the provided content in html unless ``plaintext``\n        is False.\n        Content conversion can be done in two ways:\n        - wrapping it into a pre (preserve=True)\n        - use plaintext2html (preserve=False, using container_tag to wrap the\n            whole content)\n        A side-effect of this method is to coerce all HTML tags to\n        lowercase in ``html``, and strip enclosing <html> or <body> tags in\n        content if ``plaintext`` is False.\n\n        :param str html: html tagsoup (doesn't have to be XHTML)\n        :param str content: extra content to append\n        :param bool plaintext: whether content is plaintext and should\n            be wrapped in a <pre/> tag.\n        :param bool preserve: if content is plaintext, wrap it into a <pre>\n            instead of converting it into html\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Name(id='ustr', ctx=Load()),
                        args=[Name(id='html', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='plaintext', ctx=Load()),
                            Name(id='preserve', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='\n<pre>%s</pre>\n', kind='u'),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='misc', ctx=Load()),
                                        attr='html_escape',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='ustr', ctx=Load()),
                                            args=[Name(id='content', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Name(id='plaintext', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='\n%s\n', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='plaintext2html', ctx=Load()),
                                            args=[
                                                Name(id='content', ctx=Load()),
                                                Name(id='container_tag', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='(?i)(</?(?:html|body|head|!\\s*DOCTYPE)[^>]*>)', kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='content', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='\n%s\n', kind='u'),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='ustr', ctx=Load()),
                                            args=[Name(id='content', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='(</?)(\\w+)([ >])', kind=None),
                            Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=BinOp(
                                    left=Constant(value='%s%s%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=1, kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='m', ctx=Load()),
                                                            attr='group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=2, kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=3, kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            Name(id='html', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='insert_location', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='find',
                            ctx=Load(),
                        ),
                        args=[Constant(value='</body>', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='insert_location', ctx=Load()),
                        ops=[Eq()],
                        comparators=[
                            UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='insert_location', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='find',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='</html>', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='insert_location', ctx=Load()),
                        ops=[Eq()],
                        comparators=[
                            UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='markupsafe', ctx=Load()),
                                    attr='Markup',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='html', ctx=Load()),
                                                Name(id='content', ctx=Load()),
                                            ],
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
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='markupsafe', ctx=Load()),
                            attr='Markup',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Constant(value='%s%s%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='html', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Name(id='insert_location', ctx=Load()),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Name(id='content', ctx=Load()),
                                        Subscript(
                                            value=Name(id='html', ctx=Load()),
                                            slice=Slice(
                                                lower=Name(id='insert_location', ctx=Load()),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
            name='prepend_html_content',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='html_body', annotation=None, type_comment=None),
                    arg(arg='html_content', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Prepend some HTML content at the beginning of an other HTML content.', kind=None),
                ),
                Assign(
                    targets=[Name(id='html_content', ctx=Store())],
                    value=Call(
                        func=Call(
                            func=Name(id='type', ctx=Load()),
                            args=[Name(id='html_content', ctx=Load())],
                            keywords=[],
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(?i)(</?(?:html|body|head|!\\s*DOCTYPE)[^>]*>)', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='html_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='html_content', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='html_content', ctx=Load()),
                            attr='strip',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='body_match', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<body[^>]*>', kind=None),
                                    Name(id='html_body', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<html[^>]*>', kind=None),
                                    Name(id='html_body', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='insert_index', ctx=Store())],
                    value=IfExp(
                        test=Name(id='body_match', ctx=Load()),
                        body=Call(
                            func=Attribute(
                                value=Name(id='body_match', ctx=Load()),
                                attr='end',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        orelse=Constant(value=0, kind=None),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BinOp(
                        left=BinOp(
                            left=Subscript(
                                value=Name(id='html_body', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=Name(id='insert_index', ctx=Load()),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            op=Add(),
                            right=Name(id='html_content', ctx=Load()),
                        ),
                        op=Add(),
                        right=Subscript(
                            value=Name(id='html_body', ctx=Load()),
                            slice=Slice(
                                lower=Name(id='insert_index', ctx=Load()),
                                upper=None,
                                step=None,
                            ),
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='email_re', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,63})', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='VERBOSE',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='single_email_re', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,63}$', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='VERBOSE',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='mail_header_msgid_re', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='<[^<>]+>', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='email_addr_escapes_re', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='[\\\\"]', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='generate_tracking_message_id',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='res_id', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Returns a string that can be used in the Message-ID RFC822 header field\n\n       Used to track the replies related to a given object thanks to the "In-Reply-To"\n       or "References" fields that Mail User Agents will set.\n    ', kind=None),
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='rnd', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='SystemRandom',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='random',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='NotImplementedError', ctx=Load()),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='rnd', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='random',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Assign(
                    targets=[Name(id='rndstr', ctx=Store())],
                    value=Subscript(
                        value=BinOp(
                            left=Constant(value='%.15f', kind=None),
                            op=Mod(),
                            right=Name(id='rnd', ctx=Load()),
                        ),
                        slice=Slice(
                            lower=Constant(value=2, kind=None),
                            upper=None,
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='<%s.%.15f-openerp-%s@%s>', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='rndstr', ctx=Load()),
                                Call(
                                    func=Attribute(
                                        value=Name(id='time', ctx=Load()),
                                        attr='time',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                Name(id='res_id', ctx=Load()),
                                Call(
                                    func=Attribute(
                                        value=Name(id='socket', ctx=Load()),
                                        attr='gethostname',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='email_split_tuples',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='text', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a list of (name, email) address tuples found in ``text`` . Note\n    that text should be an email header or a stringified email list as it may\n    give broader results than expected on actual text. ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='text', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=ListComp(
                        elt=Tuple(
                            elts=[
                                Subscript(
                                    value=Name(id='addr', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                Subscript(
                                    value=Name(id='addr', ctx=Load()),
                                    slice=Constant(value=1, kind=None),
                                    ctx=Load(),
                                ),
                            ],
                            ctx=Load(),
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='addr', ctx=Store()),
                                iter=Call(
                                    func=Name(id='getaddresses', ctx=Load()),
                                    args=[
                                        List(
                                            elts=[Name(id='text', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ifs=[
                                    Subscript(
                                        value=Name(id='addr', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Constant(value='@', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='addr', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                is_async=0,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='email_split',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='text', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a list of the email addresses found in ``text`` ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='text', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=ListComp(
                        elt=Name(id='email', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='name', ctx=Store()),
                                        Name(id='email', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Name(id='email_split_tuples', ctx=Load()),
                                    args=[Name(id='text', ctx=Load())],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='email_split_and_format',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='text', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a list of email addresses found in ``text``, formatted using\n    formataddr. ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='text', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=ListComp(
                        elt=Call(
                            func=Name(id='formataddr', ctx=Load()),
                            args=[
                                Tuple(
                                    elts=[
                                        Name(id='name', ctx=Load()),
                                        Name(id='email', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='name', ctx=Store()),
                                        Name(id='email', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Name(id='email_split_tuples', ctx=Load()),
                                    args=[Name(id='text', ctx=Load())],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='email_normalize',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='text', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Sanitize and standardize email address entries.\n        A normalized email is considered as :\n        - having a left part + @ + a right part (the domain can be without '.something')\n        - being lower case\n        - having no name before the address. Typically, having no 'Name <>'\n        Ex:\n        - Possible Input Email : 'Name <NaMe@DoMaIn.CoM>'\n        - Normalized Output Email : 'name@domain.com'\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='emails', ctx=Store())],
                    value=Call(
                        func=Name(id='email_split', ctx=Load()),
                        args=[Name(id='text', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='emails', ctx=Load()),
                            ),
                            Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='emails', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='emails', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            attr='lower',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='email_domain_extract',
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
                Expr(
                    value=Constant(value=' Extract the company domain to be used by IAP services notably. Domain\n    is extracted from email information e.g:\n        - info@proximus.be -> proximus.be\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='normalized_email', ctx=Store())],
                    value=Call(
                        func=Name(id='email_normalize', ctx=Load()),
                        args=[Name(id='email', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='normalized_email', ctx=Load()),
                    body=[
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='normalized_email', ctx=Load()),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='@', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
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
            name='email_domain_normalize',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='domain', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Return the domain normalized or False if the domain is invalid.', kind=None),
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='domain', ctx=Load()),
                            ),
                            Compare(
                                left=Constant(value='@', kind=None),
                                ops=[In()],
                                comparators=[Name(id='domain', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='domain', ctx=Load()),
                            attr='lower',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='url_domain_extract',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='url', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Extract the company domain to be used by IAP services notably. Domain\n    is extracted from an URL e.g:\n        - www.info.proximus.be -> proximus.be\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='parser_results', ctx=Store())],
                    value=Call(
                        func=Name(id='urlparse', ctx=Load()),
                        args=[Name(id='url', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_hostname', ctx=Store())],
                    value=Attribute(
                        value=Name(id='parser_results', ctx=Load()),
                        attr='hostname',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='company_hostname', ctx=Load()),
                            Compare(
                                left=Constant(value='.', kind=None),
                                ops=[In()],
                                comparators=[Name(id='company_hostname', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='.', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='company_hostname', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='.', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Slice(
                                            lower=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=2, kind=None),
                                            ),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
            name='email_escape_char',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='email_address', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Escape problematic characters in the given email address string', kind=None),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='email_address', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\', kind=None),
                                            Constant(value='\\\\', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%', kind=None),
                                    Constant(value='\\%', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='_', kind=None),
                            Constant(value='\\_', kind=None),
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
            name='decode_message_header',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='message', annotation=None, type_comment=None),
                    arg(arg='header', annotation=None, type_comment=None),
                    arg(arg='separator', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=' ', kind=None)],
            ),
            body=[
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='separator', ctx=Load()),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            GeneratorExp(
                                elt=Name(id='h', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='h', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='message', ctx=Load()),
                                                attr='get_all',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='header', ctx=Load()),
                                                List(elts=[], ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='h', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
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
            name='formataddr',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='pair', annotation=None, type_comment=None),
                    arg(arg='charset', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='utf-8', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Pretty format a 2-tuple of the form (realname, email_address).\n\n    If the first element of pair is falsy then only the email address\n    is returned.\n\n    Set the charset to ascii to get a RFC-2822 compliant email. The\n    realname will be base64 encoded (if necessary) and the domain part\n    of the email will be punycode encoded (if necessary). The local part\n    is left unchanged thus require the SMTPUTF8 extension when there are\n    non-ascii characters.\n\n    >>> formataddr((\'John Doe\', \'johndoe@example.com\'))\n    \'"John Doe" <johndoe@example.com>\'\n\n    >>> formataddr((\'\', \'johndoe@example.com\'))\n    \'johndoe@example.com\'\n    ', kind=None),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='name', ctx=Store()),
                                Name(id='address', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='pair', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='local', ctx=Store()),
                                Name(id='_', ctx=Store()),
                                Name(id='domain', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='address', ctx=Load()),
                            attr='rpartition',
                            ctx=Load(),
                        ),
                        args=[Constant(value='@', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='domain', ctx=Load()),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='charset', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='UnicodeEncodeError', ctx=Load()),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='idna', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ascii', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                If(
                    test=Name(id='name', ctx=Load()),
                    body=[
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='name', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='charset', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='UnicodeEncodeError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='name', ctx=Load()),
                                                                    attr='encode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='utf-8', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ascii', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=JoinedStr(
                                                values=[
                                                    Constant(value='=?utf-8?b?', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='name', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='?= <', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='local', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='@', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='domain', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='>', kind=None),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='email_addr_escapes_re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\\\\\g<0>', kind=None),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='"', kind=None),
                                            FormattedValue(
                                                value=Name(id='name', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='" <', kind=None),
                                            FormattedValue(
                                                value=Name(id='local', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='@', kind=None),
                                            FormattedValue(
                                                value=Name(id='domain', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='>', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            finalbody=[],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=JoinedStr(
                        values=[
                            FormattedValue(
                                value=Name(id='local', ctx=Load()),
                                conversion=-1,
                                format_spec=None,
                            ),
                            Constant(value='@', kind=None),
                            FormattedValue(
                                value=Name(id='domain', ctx=Load()),
                                conversion=-1,
                                format_spec=None,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='encapsulate_email',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='old_email', annotation=None, type_comment=None),
                    arg(arg='new_email', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Change the FROM of the message and use the old one as name.\n\n    e.g.\n    * Old From: "Admin" <admin@gmail.com>\n    * New From: notifications@odoo.com\n    * Output:   "Admin (admin@gmail.com)" <notifications@odoo.com>\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='old_email_split', ctx=Store())],
                    value=Call(
                        func=Name(id='getaddresses', ctx=Load()),
                        args=[
                            List(
                                elts=[Name(id='old_email', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='old_email_split', ctx=Load()),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Name(id='old_email_split', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Name(id='old_email', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='new_email_split', ctx=Store())],
                    value=Call(
                        func=Name(id='getaddresses', ctx=Load()),
                        args=[
                            List(
                                elts=[Name(id='new_email', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='new_email_split', ctx=Load()),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Name(id='new_email_split', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                If(
                    test=Subscript(
                        value=Subscript(
                            value=Name(id='old_email_split', ctx=Load()),
                            slice=Constant(value=0, kind=None),
                            ctx=Load(),
                        ),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='name_part', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s (%s)', kind=None),
                                op=Mod(),
                                right=Subscript(
                                    value=Name(id='old_email_split', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='name_part', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='old_email_split', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                Return(
                    value=Call(
                        func=Name(id='formataddr', ctx=Load()),
                        args=[
                            Tuple(
                                elts=[
                                    Name(id='name_part', ctx=Load()),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='new_email_split', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
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
    type_ignores=[],
)
