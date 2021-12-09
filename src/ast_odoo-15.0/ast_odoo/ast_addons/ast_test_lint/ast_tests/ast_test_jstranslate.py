Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules',
            names=[alias(name='get_resource_from_path', asname=None)],
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
            targets=[Name(id='TSTRING_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='_l?t\\(\\s*`.*?\\s*`\\s*\\)', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='DOTALL',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='EXPRESSION_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='\\$\\{.+?\\}', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='UNDERSCORE_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='\\b_\\(\\s*[\\\'"]', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='TestJsTranslations',
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
                    name='check_text',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Search for translation errors in the text\n\n        :param text: The js text to search\n        :return: A list of tuple with line number and invalid template string,\n                 or None for underscore errors\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='error_list', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='m', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='TSTRING_RE', ctx=Load()),
                                    attr='finditer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='text', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='template_string', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='m', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='EXPRESSION_RE', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template_string', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='line_nb', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='text', ctx=Load()),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='m', ctx=Load()),
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
                                                        attr='count',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='\n', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='error_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='line_nb', ctx=Load()),
                                                            Name(id='template_string', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
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
                        For(
                            target=Name(id='m', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='UNDERSCORE_RE', ctx=Load()),
                                    attr='finditer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='text', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lineno', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='text', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Call(
                                                            func=Attribute(
                                                                value=Name(id='m', ctx=Load()),
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
                                                attr='count',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='\n', kind=None)],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='error_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Name(id='lineno', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='error_list', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_regular_expression',
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
                            targets=[Name(id='bad_js', ctx=Store())],
                            value=Constant(value='\n        const foo = {\n            valid: _lt(`not useful but valid template-string`),\n            invalid: _lt(`invalid template-string\n            that spans multiple lines ${expression}`)\n        };\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='error_list', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_text',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bad_js', ctx=Load())],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='error_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Name(id='line', ctx=Store()),
                                                Name(id='template_string', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='error_list', ctx=Load()),
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
                                    Name(id='line', ctx=Load()),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='invalid template-string', kind=None),
                                    Name(id='template_string', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='but valid template-string', kind=None),
                                    Name(id='template_string', ctx=Load()),
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
                    name='test_regular_expression_long',
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
                            targets=[Name(id='bad_js', ctx=Store())],
                            value=Constant(value='\n        thing = _t(\n            `foo ${this + is(a, very) - long == expression}`\n        );\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='error_list', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_text',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bad_js', ctx=Load())],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='error_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Name(id='line', ctx=Store()),
                                                Name(id='template_string', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='error_list', ctx=Load()),
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
                                    Name(id='line', ctx=Load()),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo ${this + is(a, very) - long == expression}', kind=None),
                                    Name(id='template_string', ctx=Load()),
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
                    name='test_matches_underscore',
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
                            targets=[Name(id='bad_js', ctx=Store())],
                            value=Constant(value='\n        const thing1 = _(\'literal0\');\n        const thing0 = _([]);\n        const thing2 = _("literal1");\n        ', kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='check_text',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='bad_js', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=4, kind=None),
                                                    Constant(value=None, kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_js_translations',
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
                            value=Constant(value=' Test that there are no translation of JS template strings or underscore\n        calls misused as translation markers\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='counter', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='failures', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='js_file', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='iter_module_files',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='*.js', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='js_file', ctx=Load()),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/lodash.js', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Name(id='counter', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='file_open',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='js_file', ctx=Load()),
                                                    Constant(value='r', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='f', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='js_txt', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='error_list', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='check_text',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='js_txt', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='line_number', ctx=Store()),
                                            Name(id='template_string', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='error_list', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='failures', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='mod', ctx=Store()),
                                                        Name(id='relative_path', ctx=Store()),
                                                        Name(id='_', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='get_resource_from_path', ctx=Load()),
                                                args=[Name(id='js_file', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='template_string', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='prefix', ctx=Store())],
                                                    value=Constant(value='Translation of a template string', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='suffix', ctx=Store())],
                                                    value=Name(id='template_string', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='prefix', ctx=Store())],
                                                    value=Constant(value='underscore.js used as translation function', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='suffix', ctx=Store())],
                                                    value=Constant(value='_t and _lt are the JS translation functions', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='%s found in `%s/%s` at line %s: %s', kind=None),
                                                    Name(id='prefix', ctx=Load()),
                                                    Name(id='mod', ctx=Load()),
                                                    Name(id='relative_path', ctx=Load()),
                                                    Name(id='line_number', ctx=Load()),
                                                    Name(id='suffix', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%s files tested', kind=None),
                                    Name(id='counter', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='failures', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='fail',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s invalid template strings found in js files.', kind=None),
                                                op=Mod(),
                                                right=Name(id='failures', ctx=Load()),
                                            ),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
