Module(
    body=[
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module='glob',
            names=[alias(name='glob', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='logging',
            names=[alias(name='getLogger', asname=None)],
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
            module='odoo.tools',
            names=[alias(name='misc', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons',
            names=[alias(name='__path__', asname='ADDONS_PATH')],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='http', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='root', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Name(id='getLogger', ctx=Load()),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='SCRIPT_EXTENSIONS', ctx=Store())],
            value=Tuple(
                elts=[Constant(value='js', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='STYLE_EXTENSIONS', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value='css', kind=None),
                    Constant(value='scss', kind=None),
                    Constant(value='sass', kind=None),
                    Constant(value='less', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TEMPLATE_EXTENSIONS', ctx=Store())],
            value=Tuple(
                elts=[Constant(value='xml', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_SEQUENCE', ctx=Store())],
            value=Constant(value=16, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='APPEND_DIRECTIVE', ctx=Store())],
            value=Constant(value='append', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='PREPEND_DIRECTIVE', ctx=Store())],
            value=Constant(value='prepend', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='AFTER_DIRECTIVE', ctx=Store())],
            value=Constant(value='after', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='BEFORE_DIRECTIVE', ctx=Store())],
            value=Constant(value='before', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='REMOVE_DIRECTIVE', ctx=Store())],
            value=Constant(value='remove', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='REPLACE_DIRECTIVE', ctx=Store())],
            value=Constant(value='replace', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='INCLUDE_DIRECTIVE', ctx=Store())],
            value=Constant(value='include', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DIRECTIVES_WITH_TARGET', ctx=Store())],
            value=List(
                elts=[
                    Name(id='AFTER_DIRECTIVE', ctx=Load()),
                    Name(id='BEFORE_DIRECTIVE', ctx=Load()),
                    Name(id='REPLACE_DIRECTIVE', ctx=Load()),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='WILDCARD_CHARACTERS', ctx=Store())],
            value=Set(
                elts=[
                    Constant(value='*', kind=None),
                    Constant(value='?', kind=None),
                    Constant(value='[', kind=None),
                    Constant(value=']', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='fs2web',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='path', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Converts a file system path to a web path', kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='sep',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='/', kind=None)],
                    ),
                    body=[
                        Return(
                            value=Name(id='path', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value='/', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='path', ctx=Load()),
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
            name='can_aggregate',
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
                Assign(
                    targets=[Name(id='parsed', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='urls', ctx=Load()),
                            attr='url_parse',
                            ctx=Load(),
                        ),
                        args=[Name(id='url', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BoolOp(
                        op=And(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='parsed', ctx=Load()),
                                    attr='scheme',
                                    ctx=Load(),
                                ),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='parsed', ctx=Load()),
                                    attr='netloc',
                                    ctx=Load(),
                                ),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='url', ctx=Load()),
                                        attr='startswith',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='/web/content', kind=None)],
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
        FunctionDef(
            name='is_wildcard_glob',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='path', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Determine whether a path is a wildcarded glob eg: "/web/file[14].*"\n    or a genuine single file path "/web/myfile.scss', kind=None),
                ),
                Return(
                    value=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Attribute(
                                value=Name(id='WILDCARD_CHARACTERS', ctx=Load()),
                                attr='isdisjoint',
                                ctx=Load(),
                            ),
                            args=[Name(id='path', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='IrAsset',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value="This model contributes to two things:\n\n        1. It provides a function returning a list of all file paths declared\n        in a given list of addons (see _get_addon_paths);\n\n        2. It allows to create 'ir.asset' records to add additional directives\n        to certain bundles.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.asset', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Asset', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence, id', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
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
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
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
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='unlink',
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
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Name', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='bundle', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Bundle name', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='directive', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Directive', kind=None),
                            ),
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Name(id='APPEND_DIRECTIVE', ctx=Load()),
                                                Constant(value='Append', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Name(id='PREPEND_DIRECTIVE', ctx=Load()),
                                                Constant(value='Prepend', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Name(id='AFTER_DIRECTIVE', ctx=Load()),
                                                Constant(value='After', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Name(id='BEFORE_DIRECTIVE', ctx=Load()),
                                                Constant(value='Before', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Name(id='REMOVE_DIRECTIVE', ctx=Load()),
                                                Constant(value='Remove', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Name(id='REPLACE_DIRECTIVE', ctx=Load()),
                                                Constant(value='Replace', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Name(id='INCLUDE_DIRECTIVE', ctx=Load()),
                                                Constant(value='Include', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='APPEND_DIRECTIVE', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Path (or glob pattern)', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='target', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Target', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='active', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Sequence', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='DEFAULT_SEQUENCE', ctx=Load()),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_asset_paths',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='addons', annotation=None, type_comment=None),
                            arg(arg='css', annotation=None, type_comment=None),
                            arg(arg='js', annotation=None, type_comment=None),
                            arg(arg='xml', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Fetches all asset file paths from a given list of addons matching a\n        certain bundle. The returned list is composed of tuples containing the\n        file path [1], the first addon calling it [0] and the bundle name.\n        Asset loading is performed as follows:\n\n        1. All 'ir.asset' records matching the given bundle and with a sequence\n        strictly less than 16 are applied.\n\n        3. The manifests of the given addons are checked for assets declaration\n        for the given bundle. If any, they are read sequentially and their\n        operations are applied to the current list.\n\n        4. After all manifests have been parsed, the remaining 'ir.asset'\n        records matching the bundle are also applied to the current list.\n\n        :param bundle: name of the bundle from which to fetch the file paths\n        :param addons: list of addon names as strings. The files returned will\n            only be contained in the given addons.\n        :param css: boolean: whether or not to include style files\n        :param js: boolean: whether or not to include script files\n        :param xml: boolean: whether or not to include template files\n        :returns: the list of tuples (path, addon, bundle)\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='installed', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_installed_addons_list',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='addons', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='addons', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_active_addons_list',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='asset_paths', ctx=Store())],
                            value=Call(
                                func=Name(id='AssetPaths', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fill_asset_paths',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bundle', ctx=Load()),
                                    Name(id='addons', ctx=Load()),
                                    Name(id='installed', ctx=Load()),
                                    Name(id='css', ctx=Load()),
                                    Name(id='js', ctx=Load()),
                                    Name(id='xml', ctx=Load()),
                                    Name(id='asset_paths', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='asset_paths', ctx=Load()),
                                attr='list',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_fill_asset_paths',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='addons', annotation=None, type_comment=None),
                            arg(arg='installed', annotation=None, type_comment=None),
                            arg(arg='css', annotation=None, type_comment=None),
                            arg(arg='js', annotation=None, type_comment=None),
                            arg(arg='xml', annotation=None, type_comment=None),
                            arg(arg='asset_paths', annotation=None, type_comment=None),
                            arg(arg='seen', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Fills the given AssetPaths instance by applying the operations found in\n        the matching bundle of the given addons manifests.\n        See `_get_asset_paths` for more information.\n\n        :param bundle: name of the bundle from which to fetch the file paths\n        :param addons: list of addon names as strings\n        :param css: boolean: whether or not to include style files\n        :param js: boolean: whether or not to include script files\n        :param xml: boolean: whether or not to include template files\n        :param asset_paths: the AssetPath object to fill\n        :param seen: a list of bundles already checked to avoid circularity\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='bundle', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='seen', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Circular assets bundle declaration: %s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Constant(value=' > ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        BinOp(
                                                            left=Name(id='seen', ctx=Load()),
                                                            op=Add(),
                                                            right=List(
                                                                elts=[Name(id='bundle', ctx=Load())],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='root', ctx=Load()),
                                    attr='_loaded',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='root', ctx=Load()),
                                            attr='load_addons',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='root', ctx=Load()),
                                            attr='_loaded',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='manifest_cache', ctx=Store())],
                            value=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='addons_manifest',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='exts', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='js', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='exts', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='SCRIPT_EXTENSIONS', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='css', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='exts', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='STYLE_EXTENSIONS', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='xml', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='exts', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='TEMPLATE_EXTENSIONS', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='bundle_start_index', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='asset_paths', ctx=Load()),
                                        attr='list',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='process_path',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='directive', annotation=None, type_comment=None),
                                    arg(arg='target', annotation=None, type_comment=None),
                                    arg(arg='path_def', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value='\n            This sub function is meant to take a directive and a set of\n            arguments and apply them to the current asset_paths list\n            accordingly.\n\n            It is nested inside `_get_asset_paths` since we need the current\n            list of addons, extensions, asset_paths and manifest_cache.\n\n            :param directive: string\n            :param target: string or None or False\n            :param path_def: string\n            ', kind=None),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='directive', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='INCLUDE_DIRECTIVE', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_fill_asset_paths',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='path_def', ctx=Load()),
                                                    Name(id='addons', ctx=Load()),
                                                    Name(id='installed', ctx=Load()),
                                                    Name(id='css', ctx=Load()),
                                                    Name(id='js', ctx=Load()),
                                                    Name(id='xml', ctx=Load()),
                                                    Name(id='asset_paths', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='seen', ctx=Load()),
                                                        op=Add(),
                                                        right=List(
                                                            elts=[Name(id='bundle', ctx=Load())],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(value=None),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='addon', ctx=Store()),
                                                Name(id='paths', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_paths',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='path_def', ctx=Load()),
                                            Name(id='installed', ctx=Load()),
                                            Name(id='exts', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='directive', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='DIRECTIVES_WITH_TARGET', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='_', ctx=Store()),
                                                        Name(id='target_paths', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_paths',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='target', ctx=Load()),
                                                    Name(id='installed', ctx=Load()),
                                                    Name(id='exts', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='target_paths', ctx=Load()),
                                                    ),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='target', ctx=Load()),
                                                                    attr='rpartition',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            slice=Constant(value=2, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='exts', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[Return(value=None)],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='target_to_index', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[Name(id='target_paths', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Subscript(
                                                                value=Name(id='target_paths', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='target', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='target_index', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='asset_paths', ctx=Load()),
                                                    attr='index',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='target_to_index', ctx=Load()),
                                                    Name(id='addon', ctx=Load()),
                                                    Name(id='bundle', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='directive', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='APPEND_DIRECTIVE', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='asset_paths', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='paths', ctx=Load()),
                                                    Name(id='addon', ctx=Load()),
                                                    Name(id='bundle', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='directive', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Name(id='PREPEND_DIRECTIVE', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='asset_paths', ctx=Load()),
                                                            attr='insert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='paths', ctx=Load()),
                                                            Name(id='addon', ctx=Load()),
                                                            Name(id='bundle', ctx=Load()),
                                                            Name(id='bundle_start_index', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='directive', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='AFTER_DIRECTIVE', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='asset_paths', ctx=Load()),
                                                                    attr='insert',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='paths', ctx=Load()),
                                                                    Name(id='addon', ctx=Load()),
                                                                    Name(id='bundle', ctx=Load()),
                                                                    BinOp(
                                                                        left=Name(id='target_index', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='directive', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='BEFORE_DIRECTIVE', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='asset_paths', ctx=Load()),
                                                                            attr='insert',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='paths', ctx=Load()),
                                                                            Name(id='addon', ctx=Load()),
                                                                            Name(id='bundle', ctx=Load()),
                                                                            Name(id='target_index', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='directive', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='REMOVE_DIRECTIVE', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='asset_paths', ctx=Load()),
                                                                                    attr='remove',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Name(id='paths', ctx=Load()),
                                                                                    Name(id='addon', ctx=Load()),
                                                                                    Name(id='bundle', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='directive', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[Name(id='REPLACE_DIRECTIVE', ctx=Load())],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='asset_paths', ctx=Load()),
                                                                                            attr='insert',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Name(id='paths', ctx=Load()),
                                                                                            Name(id='addon', ctx=Load()),
                                                                                            Name(id='bundle', ctx=Load()),
                                                                                            Name(id='target_index', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='asset_paths', ctx=Load()),
                                                                                            attr='remove',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Name(id='target_paths', ctx=Load()),
                                                                                            Name(id='addon', ctx=Load()),
                                                                                            Name(id='bundle', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Raise(
                                                                                    exc=Call(
                                                                                        func=Name(id='ValueError', ctx=Load()),
                                                                                        args=[Constant(value='Unexpected directive', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    cause=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
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
                        Assign(
                            targets=[Name(id='assets', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_related_assets',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='bundle', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='bundle', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='active', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='asset', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='assets', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='a', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='a', ctx=Load()),
                                                attr='sequence',
                                                ctx=Load(),
                                            ),
                                            ops=[Lt()],
                                            comparators=[Name(id='DEFAULT_SEQUENCE', ctx=Load())],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='process_path', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='asset', ctx=Load()),
                                                attr='directive',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='asset', ctx=Load()),
                                                attr='target',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='asset', ctx=Load()),
                                                attr='path',
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
                        For(
                            target=Name(id='addon', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_topological_sort',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[Name(id='addons', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='manifest', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='manifest_cache', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='addon', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='manifest', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='manifest_assets', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='manifest', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='assets', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='command', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='manifest_assets', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='bundle', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='command', ctx=Load()),
                                                    Name(id='str', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='directive', ctx=Store()),
                                                                Name(id='target', ctx=Store()),
                                                                Name(id='path_def', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Tuple(
                                                        elts=[
                                                            Name(id='APPEND_DIRECTIVE', ctx=Load()),
                                                            Constant(value=None, kind=None),
                                                            Name(id='command', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='command', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='DIRECTIVES_WITH_TARGET', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Tuple(
                                                                    elts=[
                                                                        Name(id='directive', ctx=Store()),
                                                                        Name(id='target', ctx=Store()),
                                                                        Name(id='path_def', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='command', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Tuple(
                                                                    elts=[
                                                                        Name(id='directive', ctx=Store()),
                                                                        Name(id='path_def', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='command', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='target', ctx=Store())],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='process_path', ctx=Load()),
                                                args=[
                                                    Name(id='directive', ctx=Load()),
                                                    Name(id='target', ctx=Load()),
                                                    Name(id='path_def', ctx=Load()),
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
                        For(
                            target=Name(id='asset', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='assets', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='a', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='a', ctx=Load()),
                                                attr='sequence',
                                                ctx=Load(),
                                            ),
                                            ops=[GtE()],
                                            comparators=[Name(id='DEFAULT_SEQUENCE', ctx=Load())],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='process_path', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='asset', ctx=Load()),
                                                attr='directive',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='asset', ctx=Load()),
                                                attr='target',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='asset', ctx=Load()),
                                                attr='path',
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_related_assets',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Returns a set of assets matching the domain, regardless of their\n        active state. This method can be overridden to filter the results.\n        :param domain: search domain\n        :returns: ir.asset recordset\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='sequence, id', kind=None),
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
                    name='_get_related_bundle',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='target_path_def', annotation=None, type_comment=None),
                            arg(arg='root_bundle', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Returns the first bundle directly defining a glob matching the target\n        path. This is useful when generating an 'ir.asset' record to override\n        a specific asset and target the right bundle, i.e. the first one\n        defining the target path.\n\n        :param target_path_def: string: path to match.\n        :root_bundle: string: bundle from which to initiate the search.\n        :returns: the first matching bundle or None\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ext', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='target_path_def', ctx=Load()),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='.', kind=None)],
                                    keywords=[],
                                ),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='installed', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_installed_addons_list',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='target_path', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_paths',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='target_path_def', ctx=Load()),
                                            Name(id='installed', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    slice=Constant(value=1, kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='css', ctx=Store())],
                            value=Compare(
                                left=Name(id='ext', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='STYLE_EXTENSIONS', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='js', ctx=Store())],
                            value=Compare(
                                left=Name(id='ext', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='SCRIPT_EXTENSIONS', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml', ctx=Store())],
                            value=Compare(
                                left=Name(id='ext', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='TEMPLATE_EXTENSIONS', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='asset_paths', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_asset_paths',
                                    ctx=Load(),
                                ),
                                args=[Name(id='root_bundle', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='css',
                                        value=Name(id='css', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='js',
                                        value=Name(id='js', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='xml',
                                        value=Name(id='xml', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='path', ctx=Store()),
                                    Name(id='_', ctx=Store()),
                                    Name(id='bundle', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='asset_paths', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='path', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='target_path', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='bundle', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='root_bundle', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_active_addons_list',
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
                            value=Constant(value='Can be overridden to filter the returned list of active modules.', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_installed_addons_list',
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
                    name='_topological_sort',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='addons_tuple', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns a list of sorted modules name accord to the spec in ir.module.module\n        that is, application desc, sequence, name then topologically sorted', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='IrModule', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.module.module', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='mapper',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='addon', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='manif', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='http', ctx=Load()),
                                                attr='addons_manifest',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='addon', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='from_terp', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrModule', ctx=Load()),
                                            attr='get_values_from_terp',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='manif', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='from_terp', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='addon', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='from_terp', ctx=Load()),
                                            slice=Constant(value='depends', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='manif', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='depends', kind=None),
                                            List(
                                                elts=[Constant(value='base', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='from_terp', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='manifs', ctx=Store())],
                            value=Call(
                                func=Name(id='map', ctx=Load()),
                                args=[
                                    Name(id='mapper', ctx=Load()),
                                    Name(id='addons_tuple', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='sort_key',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='manif', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Name(id='manif', ctx=Load()),
                                                    slice=Constant(value='application', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='manif', ctx=Load()),
                                                        slice=Constant(value='sequence', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Name(id='manif', ctx=Load()),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='manifs', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[Name(id='manifs', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Name(id='sort_key', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='topological_sort',
                                    ctx=Load(),
                                ),
                                args=[
                                    DictComp(
                                        key=Subscript(
                                            value=Name(id='manif', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                        value=Subscript(
                                            value=Name(id='manif', ctx=Load()),
                                            slice=Constant(value='depends', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='manif', ctx=Store()),
                                                iter=Name(id='manifs', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache',
                                ctx=Load(),
                            ),
                            args=[Constant(value='addons_tuple', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_installed_addons_list',
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
                            value=Constant(value='\n        Returns the list of all installed addons.\n        :returns: string[]: list of module names\n        ', kind=None),
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        attr='_init_modules',
                                        ctx=Load(),
                                    ),
                                    op=BitOr(),
                                    right=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='conf',
                                                            ctx=Load(),
                                                        ),
                                                        attr='server_wide_modules',
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=BitOr(),
                                right=Call(
                                    func=Name(id='set', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='install_module', kind=None),
                                                List(elts=[], ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache_context',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='keys',
                                    value=Constant(value='install_module', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_paths',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path_def', annotation=None, type_comment=None),
                            arg(arg='installed', annotation=None, type_comment=None),
                            arg(arg='extensions', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Returns a list of file paths matching a given glob (path_def) as well as\n        the addon targeted by the path definition. If no file matches that glob,\n        the path definition is returned as is. This is either because the path is\n        not correctly written or because it points to a URL.\n\n        :param path_def: the definition (glob) of file paths to match\n        :param installed: the list of installed addons\n        :param extensions: a list of extensions that found files must match\n        :returns: a tuple: the addon targeted by the path definition [0] and the\n            list of file paths matching the definition [1] (or the glob itself if\n            none). Note that these paths are filtered on the given `extensions`.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='paths', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='path_url', ctx=Store())],
                            value=Call(
                                func=Name(id='fs2web', ctx=Load()),
                                args=[Name(id='path_def', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='path_parts', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='part', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='part', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='path_url', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='/', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='part', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='addon', ctx=Store())],
                            value=Subscript(
                                value=Name(id='path_parts', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='addon_manifest', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='http', ctx=Load()),
                                        attr='addons_manifest',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='addon', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='safe_path', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='addon_manifest', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='addon', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='installed', ctx=Load())],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Unallowed to fetch files from addon %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='addon', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='addons_path', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
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
                                                Subscript(
                                                    value=Name(id='addon_manifest', ctx=Load()),
                                                    slice=Constant(value='addons_path', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                            keywords=[],
                                        ),
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
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='full_path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='normpath',
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
                                                    Name(id='addons_path', ctx=Load()),
                                                    Starred(
                                                        value=Name(id='path_parts', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
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
                                            Compare(
                                                left=Name(id='addon', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='full_path', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Name(id='addons_path', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='full_path', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='addon', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='safe_path', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='paths', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='path', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='path', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='sorted', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='glob', ctx=Load()),
                                                                    args=[Name(id='full_path', ctx=Load())],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='recursive',
                                                                            value=Constant(value=True, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                FunctionDef(
                                    name='is_safe_path',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='path', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='misc', ctx=Load()),
                                                            attr='file_path',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='path', ctx=Load()),
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Name(id='SCRIPT_EXTENSIONS', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Name(id='STYLE_EXTENSIONS', ctx=Load()),
                                                                ),
                                                                op=Add(),
                                                                right=Name(id='TEMPLATE_EXTENSIONS', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Tuple(
                                                        elts=[
                                                            Name(id='ValueError', ctx=Load()),
                                                            Name(id='FileNotFoundError', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[
                                                        Return(
                                                            value=Constant(value=False, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='path', ctx=Load()),
                                                            attr='rpartition',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='TEMPLATE_EXTENSIONS', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='static_path', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='os', ctx=Load()),
                                                                    attr='path',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='normpath',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                BinOp(
                                                                    left=Constant(value='%s/static', kind=None),
                                                                    op=Mod(),
                                                                    right=Name(id='addon', ctx=Load()),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='sep',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Compare(
                                                        left=Name(id='static_path', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='path', ctx=Load())],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='len_paths', ctx=Store())],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='paths', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='paths', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='filter', ctx=Load()),
                                                args=[
                                                    Name(id='is_safe_path', ctx=Load()),
                                                    Name(id='paths', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='safe_path', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='safe_path', ctx=Load()),
                                            Compare(
                                                left=Name(id='len_paths', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='paths', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='paths', ctx=Store())],
                                    value=ListComp(
                                        elt=IfExp(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='path', ctx=Load()),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='TEMPLATE_EXTENSIONS', ctx=Load())],
                                            ),
                                            body=Name(id='path', ctx=Load()),
                                            orelse=Call(
                                                func=Name(id='fs2web', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='path', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[Name(id='addons_path', ctx=Load())],
                                                                keywords=[],
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
                                        generators=[
                                            comprehension(
                                                target=Name(id='path', ctx=Store()),
                                                iter=Name(id='paths', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='addon', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='paths', ctx=Load()),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='can_aggregate', ctx=Load()),
                                                    args=[Name(id='path_url', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='safe_path', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='is_wildcard_glob', ctx=Load()),
                                                            args=[Name(id='path_url', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='paths', ctx=Store())],
                                    value=List(
                                        elts=[Name(id='path_url', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='paths', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='msg', ctx=Store())],
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='IrAsset: the path "', kind=None),
                                            FormattedValue(
                                                value=Name(id='path_def', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='" did not resolve to anything.', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='safe_path', ctx=Load()),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='msg', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=' It may be due to security reasons.', kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='msg', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='addon', ctx=Load()),
                                    ListComp(
                                        elt=Name(id='path', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='path', ctx=Store()),
                                                iter=Name(id='paths', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='extensions', ctx=Load()),
                                                            ),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='path', ctx=Load()),
                                                                            attr='split',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    slice=UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=1, kind=None),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='extensions', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
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
        ClassDef(
            name='AssetPaths',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A list of asset paths (path, addon, bundle) with efficient operations. ', kind=None),
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
                                    attr='list',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='memo',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='index',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='addon', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns the index of the given path in the current assets list.', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='path', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='memo',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raise_not_found',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='bundle', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='index', ctx=Store()),
                                    Name(id='asset', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='list',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='asset', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='path', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='index', ctx=Load()),
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
                    name='append',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='paths', annotation=None, type_comment=None),
                            arg(arg='addon', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Appends the given paths to the current list.', kind=None),
                        ),
                        For(
                            target=Name(id='path', ctx=Store()),
                            iter=Name(id='paths', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='path', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='memo',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='list',
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='path', ctx=Load()),
                                                            Name(id='addon', ctx=Load()),
                                                            Name(id='bundle', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='memo',
                                                        ctx=Load(),
                                                    ),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='path', ctx=Load())],
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
                    name='insert',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='paths', annotation=None, type_comment=None),
                            arg(arg='addon', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='index', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Inserts the given paths to the current list at the given position.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='to_insert', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='path', ctx=Store()),
                            iter=Name(id='paths', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='path', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='memo',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='to_insert', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='path', ctx=Load()),
                                                            Name(id='addon', ctx=Load()),
                                                            Name(id='bundle', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='memo',
                                                        ctx=Load(),
                                                    ),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='path', ctx=Load())],
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
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='list',
                                        ctx=Load(),
                                    ),
                                    slice=Slice(
                                        lower=Name(id='index', ctx=Load()),
                                        upper=Name(id='index', ctx=Load()),
                                        step=None,
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='to_insert', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='remove',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='paths_to_remove', annotation=None, type_comment=None),
                            arg(arg='addon', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Removes the given paths from the current list.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='paths', ctx=Store())],
                            value=SetComp(
                                elt=Name(id='path', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='path', ctx=Store()),
                                        iter=Name(id='paths_to_remove', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Name(id='path', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='memo',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='paths', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='list',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(lower=None, upper=None, step=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=ListComp(
                                        elt=Name(id='asset', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='asset', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='list',
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='asset', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='paths', ctx=Load())],
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
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='memo',
                                                ctx=Load(),
                                            ),
                                            attr='difference_update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='paths', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(value=None),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='paths_to_remove', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raise_not_found',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='paths_to_remove', ctx=Load()),
                                            Name(id='bundle', ctx=Load()),
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
                    name='_raise_not_found',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='File(s) %s not found in bundle %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='path', ctx=Load()),
                                                Name(id='bundle', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
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
