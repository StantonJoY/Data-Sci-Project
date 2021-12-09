Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='read_manifest', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
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
            name='TestAssetsGenerateTimeCommon',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='generate_bundles',
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
                            targets=[Name(id='bundles', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='installed_module_names', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.module.module', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='installed', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='name', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='addon_path', ctx=Store()),
                            iter=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='addons',
                                    ctx=Load(),
                                ),
                                attr='__path__',
                                ctx=Load(),
                            ),
                            body=[
                                For(
                                    target=Name(id='addon', ctx=Store()),
                                    iter=Name(id='installed_module_names', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='manifest', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Name(id='read_manifest', ctx=Load()),
                                                        args=[
                                                            Name(id='addon_path', ctx=Load()),
                                                            Name(id='addon', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='assets', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='manifest', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='assets', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='assets', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='bundles', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='assets', ctx=Load()),
                                                                    attr='keys',
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
                            target=Name(id='bundle', ctx=Store()),
                            iter=Name(id='bundles', ctx=Load()),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='mute_logger', ctx=Load()),
                                                args=[Constant(value='odoo.addons.base.models.assetsbundle', kind=None)],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        For(
                                            target=Name(id='assets_type', ctx=Store()),
                                            iter=Tuple(
                                                elts=[
                                                    Constant(value='css', kind=None),
                                                    Constant(value='js', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='start_t', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='time', ctx=Load()),
                                                                    attr='time',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='css', ctx=Store())],
                                                            value=Compare(
                                                                left=Name(id='assets_type', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='css', kind=None)],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='js', ctx=Store())],
                                                            value=Compare(
                                                                left=Name(id='assets_type', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='js', kind=None)],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='ir.qweb', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_generate_asset_nodes',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='bundle', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='css',
                                                                        value=Name(id='css', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='js',
                                                                        value=Name(id='js', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Yield(
                                                                value=Tuple(
                                                                    elts=[
                                                                        JoinedStr(
                                                                            values=[
                                                                                FormattedValue(
                                                                                    value=Name(id='bundle', ctx=Load()),
                                                                                    conversion=-1,
                                                                                    format_spec=None,
                                                                                ),
                                                                                Constant(value='.', kind=None),
                                                                                FormattedValue(
                                                                                    value=Name(id='assets_type', ctx=Load()),
                                                                                    conversion=-1,
                                                                                    format_spec=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        BinOp(
                                                                            left=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='time',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            op=Sub(),
                                                                            right=Name(id='start_t', ctx=Load()),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='ValueError', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='info',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='Error detected while generating bundle %r %s', kind=None),
                                                                            Name(id='bundle', ctx=Load()),
                                                                            Name(id='assets_type', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
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
            name='TestLogsAssetsGenerateTime',
            bases=[Name(id='TestAssetsGenerateTimeCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_logs_assets_generate_time',
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
                            value=Constant(value="\n        The purpose of this test is to monitor the time of assets bundle generation.\n        This is not meant to test the generation failure, hence the try/except and the mute logger.\n        For example, 'web.assets_qweb' is contains only static xml.\n        ", kind=None),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='bundle', ctx=Store()),
                                    Name(id='duration', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='generate_bundles',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Bundle %r generated in %.2fs', kind=None),
                                            Name(id='bundle', ctx=Load()),
                                            Name(id='duration', ctx=Load()),
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
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestAssetsGenerateTime',
            bases=[Name(id='TestAssetsGenerateTimeCommon', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    This test is meant to be run nightly to ensure bundle generation does not exceed\n    a low threshold\n    ', kind=None),
                ),
                FunctionDef(
                    name='test_assets_generate_time',
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='bundle', ctx=Store()),
                                    Name(id='duration', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='generate_bundles',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='threshold', ctx=Store())],
                                    value=Constant(value=2, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertLess',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='duration', ctx=Load()),
                                            Name(id='threshold', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Bundle %r took more than %s sec', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='bundle', ctx=Load()),
                                                        Name(id='threshold', ctx=Load()),
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
                            type_comment=None,
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
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                        Constant(value='-standard', kind=None),
                        Constant(value='bundle_generation', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
