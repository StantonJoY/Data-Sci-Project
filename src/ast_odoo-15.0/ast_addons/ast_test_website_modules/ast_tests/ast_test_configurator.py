Module(
    body=[
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.iap.tools.iap_tools',
            names=[alias(name='iap_jsonrpc_mocked', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestConfigurator',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_theme_upgrade_upstream',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='iap_jsonrpc_mocked_configurator',
                            args=arguments(
                                posonlyargs=[],
                                args=[],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='endpoint', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='endpoint', ctx=Load()),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/api/website/1/configurator/industries', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='industries', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='label', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value='abbey', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='label', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=2, kind=None),
                                                                    Constant(value='aboriginal and torres strait islander organisation', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='label', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=3, kind=None),
                                                                    Constant(value='aboriginal art gallery', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='label', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=4, kind=None),
                                                                    Constant(value='abortion clinic', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='label', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=5, kind=None),
                                                                    Constant(value='abrasives supplier', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='label', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value='abundant life church', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='/api/website/2/configurator/recommended_themes', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='endpoint', ctx=Load())],
                                            ),
                                            body=[
                                                Return(
                                                    value=List(elts=[], ctx=Load()),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Constant(value='/api/website/2/configurator/custom_resources/', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='endpoint', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Dict(
                                                                keys=[Constant(value='images', kind=None)],
                                                                values=[Dict(keys=[], values=[])],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='iap_jsonrpc_mocked', ctx=Load()),
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
                            targets=[Name(id='iap_patch', ctx=Store())],
                            value=Call(
                                func=Name(id='patch', ctx=Load()),
                                args=[
                                    Constant(value='odoo.addons.iap.tools.iap_tools.iap_jsonrpc', kind=None),
                                    Name(id='iap_jsonrpc_mocked_configurator', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='iap_patch', ctx=Load()),
                                    attr='start',
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
                                    attr='addCleanup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='iap_patch', ctx=Load()),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='patcher', ctx=Store())],
                            value=Call(
                                func=Name(id='patch', ctx=Load()),
                                args=[Constant(value='odoo.addons.website.models.ir_module_module.IrModuleModule._theme_upgrade_upstream', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='wraps',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_theme_upgrade_upstream',
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
                                    value=Name(id='patcher', ctx=Load()),
                                    attr='start',
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
                                    attr='addCleanup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='patcher', ctx=Load()),
                                        attr='stop',
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
                    name='test_01_configurator_flow',
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
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/web#action=website.action_website_configuration', kind=None),
                                    Constant(value='configurator_flow', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='admin', kind=None),
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
                    func=Attribute(
                        value=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tests',
                                ctx=Load(),
                            ),
                            attr='common',
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
    ],
    type_ignores=[],
)
