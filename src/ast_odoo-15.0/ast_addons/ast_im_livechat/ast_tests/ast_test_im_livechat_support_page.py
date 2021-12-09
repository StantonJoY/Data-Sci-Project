Module(
    body=[
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestImLivechatSupportPage',
            bases=[Name(id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_load_modules',
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
                            value=Constant(value='Checks that all javascript modules load correctly on the livechat support page', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='check_js_modules', ctx=Store())],
                            value=Constant(value='\n            const { missing, failed, unloaded } = odoo.__DEBUG__.jsModules;\n            if ([missing, failed, unloaded].some(arr => arr.length)) {\n                console.error("Couldn\'t load all JS modules.", JSON.stringify({ missing, failed, unloaded }));\n            } else {\n                console.log("test successful");\n            }\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/im_livechat/support/1', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='code',
                                        value=Name(id='check_js_modules', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='ready',
                                        value=Constant(value='odoo.__DEBUG__.didLogInfo', kind=None),
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
