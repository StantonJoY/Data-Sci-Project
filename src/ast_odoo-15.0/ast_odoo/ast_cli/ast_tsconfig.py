Module(
    body=[
        Import(
            names=[alias(name='argparse', asname=None)],
        ),
        Import(
            names=[alias(name='glob', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='Command', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='MANIFEST_NAMES', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TSConfig',
            bases=[Name(id='Command', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Generates tsconfig files for javascript code', kind=None),
                ),
                FunctionDef(
                    name='__init__',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='command_name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='tsconfig', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_module_list',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=ListComp(
                                elt=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mod', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                attr='sep',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    slice=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2, kind=None),
                                    ),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='mname', ctx=Store()),
                                        iter=Name(id='MANIFEST_NAMES', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                    comprehension(
                                        target=Name(id='mod', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='glob', ctx=Load()),
                                                attr='glob',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='path', ctx=Load()),
                                                        JoinedStr(
                                                            values=[
                                                                Constant(value='*/', kind=None),
                                                                FormattedValue(
                                                                    value=Name(id='mname', ctx=Load()),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
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
                    name='clean_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/{2,}', kind=None),
                                    Constant(value='/', kind=None),
                                    Name(id='path', ctx=Load()),
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
                    name='prefix_suffix_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='prefix', annotation=None, type_comment=None),
                            arg(arg='suffix', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='clean_path',
                                    ctx=Load(),
                                ),
                                args=[
                                    JoinedStr(
                                        values=[
                                            FormattedValue(
                                                value=Name(id='prefix', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='/', kind=None),
                                            FormattedValue(
                                                value=Name(id='path', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='/', kind=None),
                                            FormattedValue(
                                                value=Name(id='suffix', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
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
                    name='remove_',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='modules', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='name', ctx=Store()),
                                    Name(id='path', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='modules', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='module', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='name', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='modules', ctx=Load()),
                                                    attr='remove',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='name', ctx=Load()),
                                                            Name(id='path', ctx=Load()),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cmdargs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='parser', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='argparse', ctx=Load()),
                                    attr='ArgumentParser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='prog',
                                        value=BinOp(
                                            left=Constant(value='%s %s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='sys', ctx=Load()),
                                                                        attr='argv',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='os', ctx=Load()),
                                                                        attr='path',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='sep',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        slice=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='command_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='description',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='__doc__',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--addons-path', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='type',
                                        value=Name(id='str', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='nargs',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='paths', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='parse_args',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='args',
                                        value=Name(id='cmdargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='paths', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='map', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='clean_path',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='args', ctx=Load()),
                                                            attr='paths',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=',', kind=None)],
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
                            targets=[Name(id='modules', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='path', ctx=Store()),
                            iter=Name(id='paths', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='module', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_module_list',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='modules', ctx=Load()),
                                                    slice=Name(id='module', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='prefix_suffix_path',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='module', ctx=Load()),
                                                    Name(id='path', ctx=Load()),
                                                    Constant(value='/static/src/*', kind=None),
                                                ],
                                                keywords=[],
                                            ),
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
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='generate_file_content',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='modules', ctx=Load()),
                                    Name(id='paths', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='indent',
                                                value=Constant(value=2, kind=None),
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
                    name='generate_imports',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='modules', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=DictComp(
                                key=JoinedStr(
                                    values=[
                                        Constant(value='@', kind=None),
                                        FormattedValue(
                                            value=Name(id='module', ctx=Load()),
                                            conversion=-1,
                                            format_spec=None,
                                        ),
                                        Constant(value='/*', kind=None),
                                    ],
                                ),
                                value=List(
                                    elts=[Name(id='path', ctx=Load())],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='module', ctx=Store()),
                                                Name(id='path', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='modules', ctx=Load()),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='generate_file_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='modules', annotation=None, type_comment=None),
                            arg(arg='paths', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='compilerOptions', kind=None),
                                    Constant(value='exclude', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='baseUrl', kind=None),
                                            Constant(value='target', kind=None),
                                            Constant(value='checkJs', kind=None),
                                            Constant(value='allowJs', kind=None),
                                            Constant(value='noEmit', kind=None),
                                            Constant(value='typeRoots', kind=None),
                                            Constant(value='paths', kind=None),
                                        ],
                                        values=[
                                            Constant(value='.', kind=None),
                                            Constant(value='es2019', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='map', ctx=Load()),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=BinOp(
                                                                    left=Name(id='p', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value='/web/tooling/types', kind=None),
                                                                ),
                                                            ),
                                                            Name(id='paths', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='generate_imports',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='modules', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='generate_excludes',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
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
                    name='generate_excludes',
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
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='/**/*.po', kind=None),
                                    Constant(value='/**/*.py', kind=None),
                                    Constant(value='/**/*.pyc', kind=None),
                                    Constant(value='/**/*.xml', kind=None),
                                    Constant(value='/**/*.png', kind=None),
                                    Constant(value='/**/*.md', kind=None),
                                    Constant(value='/**/*.dat', kind=None),
                                    Constant(value='/**/*.scss', kind=None),
                                    Constant(value='/**/*.jpg', kind=None),
                                    Constant(value='/**/*.svg', kind=None),
                                    Constant(value='/**/*.pot', kind=None),
                                    Constant(value='/**/*.csv', kind=None),
                                    Constant(value='/**/*.mo', kind=None),
                                    Constant(value='/**/*.txt', kind=None),
                                    Constant(value='/**/*.less', kind=None),
                                    Constant(value='/**/*.bcmap', kind=None),
                                    Constant(value='/**/*.properties', kind=None),
                                    Constant(value='/**/*.html', kind=None),
                                    Constant(value='/**/*.ttf', kind=None),
                                    Constant(value='/**/*.rst', kind=None),
                                    Constant(value='/**/*.css', kind=None),
                                    Constant(value='/**/*.pack', kind=None),
                                    Constant(value='/**/*.idx', kind=None),
                                    Constant(value='/**/*.h', kind=None),
                                    Constant(value='/**/*.map', kind=None),
                                    Constant(value='/**/*.gif', kind=None),
                                    Constant(value='/**/*.sample', kind=None),
                                    Constant(value='/**/*.doctree', kind=None),
                                    Constant(value='/**/*.so', kind=None),
                                    Constant(value='/**/*.pdf', kind=None),
                                    Constant(value='/**/*.xslt', kind=None),
                                    Constant(value='/**/*.conf', kind=None),
                                    Constant(value='/**/*.woff', kind=None),
                                    Constant(value='/**/*.xsd', kind=None),
                                    Constant(value='/**/*.eot', kind=None),
                                    Constant(value='/**/*.jst', kind=None),
                                    Constant(value='/**/*.flow', kind=None),
                                    Constant(value='/**/*.sh', kind=None),
                                    Constant(value='/**/*.yml', kind=None),
                                    Constant(value='/**/*.pfb', kind=None),
                                    Constant(value='/**/*.jpeg', kind=None),
                                    Constant(value='/**/*.crt', kind=None),
                                    Constant(value='/**/*.template', kind=None),
                                    Constant(value='/**/*.pxd', kind=None),
                                    Constant(value='/**/*.dylib', kind=None),
                                    Constant(value='/**/*.pem', kind=None),
                                    Constant(value='/**/*.rng', kind=None),
                                    Constant(value='/**/*.xsl', kind=None),
                                    Constant(value='/**/*.xls', kind=None),
                                    Constant(value='/**/*.cfg', kind=None),
                                    Constant(value='/**/*.pyi', kind=None),
                                    Constant(value='/**/*.pth', kind=None),
                                    Constant(value='/**/*.markdown', kind=None),
                                    Constant(value='/**/*.key', kind=None),
                                    Constant(value='/**/*.ico', kind=None),
                                ],
                                ctx=Load(),
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
